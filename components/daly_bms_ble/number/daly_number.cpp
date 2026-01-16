#include "daly_number.h"
#include "esphome/core/log.h"
#include "esphome/core/application.h"

namespace esphome {
namespace daly_bms_ble {

static const char *const TAG = "daly_bms_ble.number";

static const uint8_t DALY_FUNCTION_WRITE = 0x06;
static const uint8_t DALY_FUNCTION_READ = 0x03;

// Register addresses requiring special encoding
static const uint16_t DALY_REG_CHARGING_CURRENT_HIGH_WARNING = 0x0093;
static const uint16_t DALY_REG_CHARGING_CURRENT_HIGH_CRITICAL = 0x0094;
static const uint16_t DALY_REG_DISCHARGING_CURRENT_HIGH_WARNING = 0x0095;
static const uint16_t DALY_REG_DISCHARGING_CURRENT_HIGH_CRITICAL = 0x0096;

static const uint16_t DALY_REG_CHARGING_TEMP_HIGH_WARNING = 0x0097;
static const uint16_t DALY_REG_CHARGING_TEMP_HIGH_CRITICAL = 0x0098;
static const uint16_t DALY_REG_CHARGING_TEMP_LOW_WARNING = 0x0099;
static const uint16_t DALY_REG_CHARGING_TEMP_LOW_CRITICAL = 0x009A;
static const uint16_t DALY_REG_DISCHARGING_TEMP_HIGH_WARNING = 0x009B;
static const uint16_t DALY_REG_DISCHARGING_TEMP_HIGH_CRITICAL = 0x009C;
static const uint16_t DALY_REG_DISCHARGING_TEMP_LOW_WARNING = 0x009D;
static const uint16_t DALY_REG_DISCHARGING_TEMP_LOW_CRITICAL = 0x009E;
static const uint16_t DALY_REG_MOS_TEMP_PROTECTION = 0x00A8;

static const uint16_t DALY_REG_RATED_CAPACITY = 0x0080;
static const uint16_t DALY_REG_TOTAL_VOLTAGE_HIGH_WARNING = 0x008F;
static const uint16_t DALY_REG_TOTAL_VOLTAGE_HIGH_CRITICAL = 0x0090;
static const uint16_t DALY_REG_TOTAL_VOLTAGE_LOW_WARNING = 0x0091;
static const uint16_t DALY_REG_TOTAL_VOLTAGE_LOW_CRITICAL = 0x0092;
static const uint16_t DALY_REG_SOC_SETTING = 0x00A7;

void DalyNumber::dump_config() { LOG_NUMBER("", "DalyBmsBle Number", this); }

void DalyNumber::control(float value) {
  uint16_t register_value;

  // Temperature registers: add +40 offset (user provides real temperature like -20°C, we write as 20)
  if (this->holding_register_ >= DALY_REG_CHARGING_TEMP_HIGH_WARNING &&
      this->holding_register_ <= DALY_REG_DISCHARGING_TEMP_LOW_CRITICAL) {
    register_value = (uint16_t) (value + 40);
  }
  // MOS temperature protection: add +40 offset
  else if (this->holding_register_ == DALY_REG_MOS_TEMP_PROTECTION) {
    register_value = (uint16_t) (value + 40);
  }
  // Current registers: add 30000 offset and multiply by 10 (user provides real current like 10.5A, we write as 30105)
  else if (this->holding_register_ >= DALY_REG_CHARGING_CURRENT_HIGH_WARNING &&
           this->holding_register_ <= DALY_REG_DISCHARGING_CURRENT_HIGH_CRITICAL) {
    register_value = (uint16_t) ((value * 10.0f) + 30000);
  }
  // Rated capacity: multiply by 10 (user provides 100.5 Ah, we write as 1005)
  else if (this->holding_register_ == DALY_REG_RATED_CAPACITY) {
    register_value = (uint16_t) (value * 10.0f);
  }
  // Total voltage registers: multiply by 10 (user provides 14.5V, we write as 145)
  else if (this->holding_register_ >= DALY_REG_TOTAL_VOLTAGE_HIGH_WARNING &&
           this->holding_register_ <= DALY_REG_TOTAL_VOLTAGE_LOW_CRITICAL) {
    register_value = (uint16_t) (value * 10.0f);
  }
  // SOC setting: multiply by 10 (user provides 50.5%, we write as 505)
  else if (this->holding_register_ == DALY_REG_SOC_SETTING) {
    register_value = (uint16_t) (value * 10.0f);
  }
  // All other registers: direct value (mV, counts, etc.)
  else {
    register_value = (uint16_t) value;
  }

  ESP_LOGD(TAG, "Setting register 0x%04X to %d (from user value %.2f)", this->holding_register_, register_value, value);

  if (this->parent_->send_command(DALY_FUNCTION_WRITE, this->holding_register_, register_value)) {
    this->publish_state(value);
    
    // Schedule a readback after 500ms to verify the value was set correctly
    this->set_timeout("verify_write", 500, [this]() {
      ESP_LOGD(TAG, "Requesting settings readback to verify write");
      this->parent_->request_settings();
    });
  }
}

}  // namespace daly_bms_ble
}  // namespace esphome
