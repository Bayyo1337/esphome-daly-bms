#pragma once

#include "esphome/core/component.h"
#include "esphome/components/ble_client/ble_client.h"
#include "esphome/components/esp32_ble_tracker/esp32_ble_tracker. h"
#include "esphome/components/binary_sensor/binary_sensor.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/switch/switch.h"
#include "esphome/components/text_sensor/text_sensor.h"
#include "esphome/components/number/number.h"

#ifdef USE_ESP32

#include <esp_gattc_api.h>

namespace esphome {
namespace daly_bms_ble {

namespace espbt = esphome::esp32_ble_tracker;

class DalyBmsBle : public esphome::ble_client:: BLEClientNode, public PollingComponent {
 public:
  void gattc_event_handler(esp_gattc_cb_event_t event, esp_gatt_if_t gattc_if,
                           esp_ble_gattc_cb_param_t *param) override;
  void dump_config() override;
  void update() override;
  float get_setup_priority() const override { return setup_priority::DATA; }

  void set_balancing_binary_sensor(binary_sensor::BinarySensor *balancing_binary_sensor) {
    balancing_binary_sensor_ = balancing_binary_sensor;
  }
  void set_charging_binary_sensor(binary_sensor::BinarySensor *charging_binary_sensor) {
    charging_binary_sensor_ = charging_binary_sensor;
  }
  void set_discharging_binary_sensor(binary_sensor:: BinarySensor *discharging_binary_sensor) {
    discharging_binary_sensor_ = discharging_binary_sensor;
  }

  void set_total_voltage_sensor(sensor:: Sensor *total_voltage_sensor) { total_voltage_sensor_ = total_voltage_sensor; }
  void set_current_sensor(sensor::Sensor *current_sensor) { current_sensor_ = current_sensor; }
  void set_power_sensor(sensor::Sensor *power_sensor) { power_sensor_ = power_sensor; }
  void set_charging_power_sensor(sensor::Sensor *charging_power_sensor) {
    charging_power_sensor_ = charging_power_sensor;
  }
  void set_discharging_power_sensor(sensor:: Sensor *discharging_power_sensor) {
    discharging_power_sensor_ = discharging_power_sensor;
  }
  void set_error_bitmask_sensor(sensor::Sensor *error_bitmask_sensor) { error_bitmask_sensor_ = error_bitmask_sensor; }
  void set_state_of_charge_sensor(sensor::Sensor *state_of_charge_sensor) {
    state_of_charge_sensor_ = state_of_charge_sensor;
  }
  void set_charging_cycles_sensor(sensor::Sensor *charging_cycles_sensor) {
    charging_cycles_sensor_ = charging_cycles_sensor;
  }
  void set_min_cell_voltage_sensor(sensor:: Sensor *min_cell_voltage_sensor) {
    min_cell_voltage_sensor_ = min_cell_voltage_sensor;
  }
  void set_max_cell_voltage_sensor(sensor::Sensor *max_cell_voltage_sensor) {
    max_cell_voltage_sensor_ = max_cell_voltage_sensor;
  }
  void set_min_voltage_cell_sensor(sensor::Sensor *min_voltage_cell_sensor) {
    min_voltage_cell_sensor_ = min_voltage_cell_sensor;
  }
  void set_max_voltage_cell_sensor(sensor::Sensor *max_voltage_cell_sensor) {
    max_voltage_cell_sensor_ = max_voltage_cell_sensor;
  }
  void set_delta_cell_voltage_sensor(sensor:: Sensor *delta_cell_voltage_sensor) {
    delta_cell_voltage_sensor_ = delta_cell_voltage_sensor;
  }
  void set_average_cell_voltage_sensor(sensor:: Sensor *average_cell_voltage_sensor) {
    average_cell_voltage_sensor_ = average_cell_voltage_sensor;
  }
  void set_cell_voltage_sensor(uint8_t cell, sensor::Sensor *cell_voltage_sensor) {
    this->cells_[cell]. cell_voltage_sensor_ = cell_voltage_sensor;
  }
  void set_temperature_sensor(uint8_t temperature, sensor::Sensor *temperature_sensor) {
    this->temperatures_[temperature].temperature_sensor_ = temperature_sensor;
  }
  void set_cell_count_sensor(sensor::Sensor *cell_count_sensor) { cell_count_sensor_ = cell_count_sensor; }
  void set_temperature_sensors_sensor(sensor::Sensor *temperature_sensors_sensor) {
    temperature_sensors_sensor_ = temperature_sensors_sensor;
  }
  void set_capacity_remaining_sensor(sensor::Sensor *capacity_remaining_sensor) {
    capacity_remaining_sensor_ = capacity_remaining_sensor;
  }

  void set_battery_status_text_sensor(text_sensor::TextSensor *battery_status_text_sensor) {
    battery_status_text_sensor_ = battery_status_text_sensor;
  }
  void set_errors_text_sensor(text_sensor::TextSensor *errors_text_sensor) { errors_text_sensor_ = errors_text_sensor; }

  void set_balancer_switch(switch_::Switch *balancer_switch) { balancer_switch_ = balancer_switch; }
  void set_charging_switch(switch_::Switch *charging_switch) { charging_switch_ = charging_switch; }
  void set_discharging_switch(switch_::Switch *discharging_switch) { discharging_switch_ = discharging_switch; }

  // Number entity setters
  void set_rated_capacity_number(number::Number *n) { rated_capacity_number_ = n; }
  void set_cell_reference_voltage_number(number::Number *n) { cell_reference_voltage_number_ = n; }
  void set_collect_boards_num_number(number::Number *n) { collect_boards_num_number_ = n; }
  void set_board_1_cell_num_number(number::Number *n) { board_1_cell_num_number_ = n; }
  void set_board_2_cell_num_number(number::Number *n) { board_2_cell_num_number_ = n; }
  void set_board_3_cell_num_number(number::Number *n) { board_3_cell_num_number_ = n; }
  void set_board_1_temp_num_number(number::Number *n) { board_1_temp_num_number_ = n; }
  void set_board_2_temp_num_number(number::Number *n) { board_2_temp_num_number_ = n; }
  void set_board_3_temp_num_number(number::Number *n) { board_3_temp_num_number_ = n; }
  void set_battery_type_number(number::Number *n) { battery_type_number_ = n; }
  void set_sleep_waiting_time_number(number::Number *n) { sleep_waiting_time_number_ = n; }
  void set_cell_voltage_high_warning_number(number::Number *n) { cell_voltage_high_warning_number_ = n; }
  void set_cell_voltage_high_critical_number(number::Number *n) { cell_voltage_high_critical_number_ = n; }
  void set_cell_voltage_low_warning_number(number::Number *n) { cell_voltage_low_warning_number_ = n; }
  void set_cell_voltage_low_critical_number(number::Number *n) { cell_voltage_low_critical_number_ = n; }
  void set_total_voltage_high_warning_number(number::Number *n) { total_voltage_high_warning_number_ = n; }
  void set_total_voltage_high_critical_number(number::Number *n) { total_voltage_high_critical_number_ = n; }
  void set_total_voltage_low_warning_number(number::Number *n) { total_voltage_low_warning_number_ = n; }
  void set_total_voltage_low_critical_number(number::Number *n) { total_voltage_low_critical_number_ = n; }
  void set_charging_current_high_warning_number(number::Number *n) { charging_current_high_warning_number_ = n; }
  void set_charging_current_high_critical_number(number::Number *n) { charging_current_high_critical_number_ = n; }
  void set_discharging_current_high_warning_number(number::Number *n) { discharging_current_high_warning_number_ = n; }
  void set_discharging_current_high_critical_number(number::Number *n) { discharging_current_high_critical_number_ = n; }
  void set_charging_temp_high_warning_number(number::Number *n) { charging_temp_high_warning_number_ = n; }
  void set_charging_temp_high_critical_number(number::Number *n) { charging_temp_high_critical_number_ = n; }
  void set_charging_temp_low_warning_number(number::Number *n) { charging_temp_low_warning_number_ = n; }
  void set_charging_temp_low_critical_number(number::Number *n) { charging_temp_low_critical_number_ = n; }
  void set_discharging_temp_high_warning_number(number::Number *n) { discharging_temp_high_warning_number_ = n; }
  void set_discharging_temp_high_critical_number(number::Number *n) { discharging_temp_high_critical_number_ = n; }
  void set_discharging_temp_low_warning_number(number::Number *n) { discharging_temp_low_warning_number_ = n; }
  void set_discharging_temp_low_critical_number(number::Number *n) { discharging_temp_low_critical_number_ = n; }
  void set_excessive_voltage_diff_warning_number(number::Number *n) { excessive_voltage_diff_warning_number_ = n; }
  void set_excessive_voltage_diff_critical_number(number::Number *n) { excessive_voltage_diff_critical_number_ = n; }
  void set_excessive_temp_diff_warning_number(number::Number *n) { excessive_temp_diff_warning_number_ = n; }
  void set_excessive_temp_diff_critical_number(number::Number *n) { excessive_temp_diff_critical_number_ = n; }
  void set_balancing_turn_on_voltage_number(number::Number *n) { balancing_turn_on_voltage_number_ = n; }
  void set_balancing_voltage_diff_number(number::Number *n) { balancing_voltage_diff_number_ = n; }
  void set_soc_setting_number(number::Number *n) { soc_setting_number_ = n; }
  void set_mos_temp_protection_number(number::Number *n) { mos_temp_protection_number_ = n; }

  void on_daly_bms_ble_data(const std::vector<uint8_t> &data);
  bool send_command(uint8_t function, uint16_t address, uint16_t value);
  void set_password(uint32_t password) { this->password_ = password; }
  void request_settings();

 protected:
  binary_sensor::BinarySensor *balancing_binary_sensor_;
  binary_sensor::BinarySensor *charging_binary_sensor_;
  binary_sensor::BinarySensor *discharging_binary_sensor_;

  sensor::Sensor *total_voltage_sensor_;
  sensor:: Sensor *current_sensor_;
  sensor::Sensor *power_sensor_;
  sensor::Sensor *charging_power_sensor_;
  sensor::Sensor *discharging_power_sensor_;
  sensor::Sensor *error_bitmask_sensor_;
  sensor::Sensor *state_of_charge_sensor_;
  sensor:: Sensor *charging_cycles_sensor_;
  sensor::Sensor *min_cell_voltage_sensor_;
  sensor::Sensor *max_cell_voltage_sensor_;
  sensor::Sensor *min_voltage_cell_sensor_;
  sensor::Sensor *max_voltage_cell_sensor_;
  sensor::Sensor *delta_cell_voltage_sensor_;
  sensor:: Sensor *average_cell_voltage_sensor_;
  sensor:: Sensor *cell_count_sensor_;
  sensor:: Sensor *temperature_sensors_sensor_;
  sensor::Sensor *capacity_remaining_sensor_;

  switch_::Switch *balancer_switch_;
  switch_::Switch *charging_switch_;
  switch_::Switch *discharging_switch_;

  text_sensor::TextSensor *battery_status_text_sensor_;
  text_sensor::TextSensor *errors_text_sensor_;

  // Number entities for configuration parameters  
  number::Number *rated_capacity_number_{nullptr};
  number::Number *cell_reference_voltage_number_{nullptr};
  number::Number *collect_boards_num_number_{nullptr};
  number::Number *board_1_cell_num_number_{nullptr};
  number:: Number *board_2_cell_num_number_{nullptr};
  number::Number *board_3_cell_num_number_{nullptr};
  number::Number *board_1_temp_num_number_{nullptr};
  number::Number *board_2_temp_num_number_{nullptr};
  number:: Number *board_3_temp_num_number_{nullptr};
  number::Number *battery_type_number_{nullptr};
  number:: Number *sleep_waiting_time_number_{nullptr};
  number:: Number *cell_voltage_high_warning_number_{nullptr};
  number::Number *cell_voltage_high_critical_number_{nullptr};
  number::Number *cell_voltage_low_warning_number_{nullptr};
  number::Number *cell_voltage_low_critical_number_{nullptr};
  number:: Number *total_voltage_high_warning_number_{nullptr};
  number::Number *total_voltage_high_critical_number_{nullptr};
  number::Number *total_voltage_low_warning_number_{nullptr};
  number::Number *total_voltage_low_critical_number_{nullptr};
  number:: Number *charging_current_high_warning_number_{nullptr};
  number::Number *charging_current_high_critical_number_{nullptr};
  number::Number *discharging_current_high_warning_number_{nullptr};
  number::Number *discharging_current_high_critical_number_{nullptr};
  number::Number *charging_temp_high_warning_number_{nullptr};
  number::Number *charging_temp_high_critical_number_{nullptr};
  number::Number *charging_temp_low_warning_number_{nullptr};
  number::Number *charging_temp_low_critical_number_{nullptr};
  number::Number *discharging_temp_high_warning_number_{nullptr};
  number::Number *discharging_temp_high_critical_number_{nullptr};
  number::Number *discharging_temp_low_warning_number_{nullptr};
  number::Number *discharging_temp_low_critical_number_{nullptr};
  number::Number *excessive_voltage_diff_warning_number_{nullptr};
  number::Number *excessive_voltage_diff_critical_number_{nullptr};
  number::Number *excessive_temp_diff_warning_number_{nullptr};
  number::Number *excessive_temp_diff_critical_number_{nullptr};
  number::Number *balancing_turn_on_voltage_number_{nullptr};
  number:: Number *balancing_voltage_diff_number_{nullptr};
  number::Number *soc_setting_number_{nullptr};
  number:: Number *mos_temp_protection_number_{nullptr};

  struct Cell {
    sensor::Sensor *cell_voltage_sensor_{nullptr};
  } cells_[32];

  struct Temperature {
    sensor::Sensor *temperature_sensor_{nullptr};
  } temperatures_[8];

  uint16_t char_notify_handle_;
  uint16_t char_command_handle_;
  uint32_t password_ = 12345678;
  uint32_t last_settings_request_ = 0;

  void decode_status_data_(const std::vector<uint8_t> &data);
  void decode_settings_data_(const std::vector<uint8_t> &data);
  void decode_version_data_(const std::vector<uint8_t> &data);
  void decode_password_data_(const std::vector<uint8_t> &data);
  void publish_state_(binary_sensor::BinarySensor *binary_sensor, const bool &state);
  void publish_state_(sensor::Sensor *sensor, float value);
  void publish_state_(switch_::Switch *obj, const bool &state);
  void publish_state_(text_sensor::TextSensor *text_sensor, const std::string &state);
  void publish_state_(number::Number *number, float value);
  std::string bitmask_to_string_(const char *const messages[], const uint8_t &messages_size, const uint64_t &mask);

  bool check_bit_(uint16_t mask, uint16_t flag) { return (mask & flag) == flag; }
};

}  // namespace daly_bms_ble
}  // namespace esphome

#endif
