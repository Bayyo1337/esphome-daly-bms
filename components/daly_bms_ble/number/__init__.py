import esphome.codegen as cg
from esphome.components import number
import esphome.config_validation as cv
from esphome.const import (
    CONF_ID,
    UNIT_AMPERE,
    UNIT_CELSIUS,
    UNIT_EMPTY,
    UNIT_SECOND,
    UNIT_VOLT,
    DEVICE_CLASS_VOLTAGE,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_EMPTY,
)

from .. import CONF_DALY_BMS_BLE_ID, DALY_BMS_BLE_COMPONENT_SCHEMA, daly_bms_ble_ns

DEPENDENCIES = ["daly_bms_ble"]
CODEOWNERS = ["@syssi"]

CONF_RATED_CAPACITY = "rated_capacity"
CONF_CELL_REFERENCE_VOLTAGE = "cell_reference_voltage"
CONF_COLLECT_BOARDS_NUM = "collect_boards_num"
CONF_BOARD_1_CELL_NUM = "board_1_cell_num"
CONF_BOARD_2_CELL_NUM = "board_2_cell_num"
CONF_BOARD_3_CELL_NUM = "board_3_cell_num"
CONF_BOARD_1_TEMP_NUM = "board_1_temp_num"
CONF_BOARD_2_TEMP_NUM = "board_2_temp_num"
CONF_BOARD_3_TEMP_NUM = "board_3_temp_num"
CONF_BATTERY_TYPE = "battery_type"
CONF_SLEEP_WAITING_TIME = "sleep_waiting_time"

# Protection parameters - Cell Voltage
CONF_CELL_VOLTAGE_HIGH_WARNING = "cell_voltage_high_warning"
CONF_CELL_VOLTAGE_HIGH_CRITICAL = "cell_voltage_high_critical"
CONF_CELL_VOLTAGE_LOW_WARNING = "cell_voltage_low_warning"
CONF_CELL_VOLTAGE_LOW_CRITICAL = "cell_voltage_low_critical"

# Protection parameters - Total Voltage
CONF_TOTAL_VOLTAGE_HIGH_WARNING = "total_voltage_high_warning"
CONF_TOTAL_VOLTAGE_HIGH_CRITICAL = "total_voltage_high_critical"
CONF_TOTAL_VOLTAGE_LOW_WARNING = "total_voltage_low_warning"
CONF_TOTAL_VOLTAGE_LOW_CRITICAL = "total_voltage_low_critical"

# Protection parameters - Current
CONF_CHARGING_CURRENT_HIGH_WARNING = "charging_current_high_warning"
CONF_CHARGING_CURRENT_HIGH_CRITICAL = "charging_current_high_critical"
CONF_DISCHARGING_CURRENT_HIGH_WARNING = "discharging_current_high_warning"
CONF_DISCHARGING_CURRENT_HIGH_CRITICAL = "discharging_current_high_critical"

# Protection parameters - Charging Temperature
CONF_CHARGING_TEMP_HIGH_WARNING = "charging_temp_high_warning"
CONF_CHARGING_TEMP_HIGH_CRITICAL = "charging_temp_high_critical"
CONF_CHARGING_TEMP_LOW_WARNING = "charging_temp_low_warning"
CONF_CHARGING_TEMP_LOW_CRITICAL = "charging_temp_low_critical"

# Protection parameters - Discharging Temperature
CONF_DISCHARGING_TEMP_HIGH_WARNING = "discharging_temp_high_warning"
CONF_DISCHARGING_TEMP_HIGH_CRITICAL = "discharging_temp_high_critical"
CONF_DISCHARGING_TEMP_LOW_WARNING = "discharging_temp_low_warning"
CONF_DISCHARGING_TEMP_LOW_CRITICAL = "discharging_temp_low_critical"

# Protection parameters - Differential
CONF_EXCESSIVE_VOLTAGE_DIFF_WARNING = "excessive_voltage_diff_warning"
CONF_EXCESSIVE_VOLTAGE_DIFF_CRITICAL = "excessive_voltage_diff_critical"
CONF_EXCESSIVE_TEMP_DIFF_WARNING = "excessive_temp_diff_warning"
CONF_EXCESSIVE_TEMP_DIFF_CRITICAL = "excessive_temp_diff_critical"

# Balance parameters
CONF_BALANCING_TURN_ON_VOLTAGE = "balancing_turn_on_voltage"
CONF_BALANCING_VOLTAGE_DIFF = "balancing_voltage_diff"

# SOC parameter
CONF_SOC_SETTING = "soc_setting"

# MOS temperature
CONF_MOS_TEMP_PROTECTION = "mos_temp_protection"

DalyNumber = daly_bms_ble_ns.class_("DalyNumber", number.Number, cg.Component)

# Register addresses from decode_settings_data_
NUMBERS = {
    CONF_RATED_CAPACITY: 0x0080,
    CONF_CELL_REFERENCE_VOLTAGE: 0x0081,
    CONF_COLLECT_BOARDS_NUM: 0x0082,
    CONF_BOARD_1_CELL_NUM: 0x0083,
    CONF_BOARD_2_CELL_NUM: 0x0084,
    CONF_BOARD_3_CELL_NUM: 0x0085,
    CONF_BOARD_1_TEMP_NUM: 0x0086,
    CONF_BOARD_2_TEMP_NUM: 0x0087,
    CONF_BOARD_3_TEMP_NUM: 0x0088,
    CONF_BATTERY_TYPE: 0x0089,
    CONF_SLEEP_WAITING_TIME: 0x008A,
    CONF_CELL_VOLTAGE_HIGH_WARNING: 0x008B,
    CONF_CELL_VOLTAGE_HIGH_CRITICAL: 0x008C,
    CONF_CELL_VOLTAGE_LOW_WARNING: 0x008D,
    CONF_CELL_VOLTAGE_LOW_CRITICAL: 0x008E,
    CONF_TOTAL_VOLTAGE_HIGH_WARNING: 0x008F,
    CONF_TOTAL_VOLTAGE_HIGH_CRITICAL: 0x0090,
    CONF_TOTAL_VOLTAGE_LOW_WARNING: 0x0091,
    CONF_TOTAL_VOLTAGE_LOW_CRITICAL: 0x0092,
    CONF_CHARGING_CURRENT_HIGH_WARNING: 0x0093,
    CONF_CHARGING_CURRENT_HIGH_CRITICAL: 0x0094,
    CONF_DISCHARGING_CURRENT_HIGH_WARNING: 0x0095,
    CONF_DISCHARGING_CURRENT_HIGH_CRITICAL: 0x0096,
    CONF_CHARGING_TEMP_HIGH_WARNING: 0x0097,
    CONF_CHARGING_TEMP_HIGH_CRITICAL: 0x0098,
    CONF_CHARGING_TEMP_LOW_WARNING: 0x0099,
    CONF_CHARGING_TEMP_LOW_CRITICAL: 0x009A,
    CONF_DISCHARGING_TEMP_HIGH_WARNING: 0x009B,
    CONF_DISCHARGING_TEMP_HIGH_CRITICAL: 0x009C,
    CONF_DISCHARGING_TEMP_LOW_WARNING: 0x009D,
    CONF_DISCHARGING_TEMP_LOW_CRITICAL: 0x009E,
    CONF_EXCESSIVE_VOLTAGE_DIFF_WARNING: 0x009F,
    CONF_EXCESSIVE_VOLTAGE_DIFF_CRITICAL: 0x00A0,
    CONF_EXCESSIVE_TEMP_DIFF_WARNING: 0x00A1,
    CONF_EXCESSIVE_TEMP_DIFF_CRITICAL: 0x00A2,
    CONF_BALANCING_TURN_ON_VOLTAGE: 0x00A3,
    CONF_BALANCING_VOLTAGE_DIFF: 0x00A4,
    CONF_SOC_SETTING: 0x00A7,
    CONF_MOS_TEMP_PROTECTION: 0x00A8,
}

CONFIG_SCHEMA = DALY_BMS_BLE_COMPONENT_SCHEMA.extend(
    {
        # Cell Characteristics
        cv.Optional(CONF_RATED_CAPACITY): number.number_schema(
            DalyNumber,
            unit_of_measurement="Ah",
            device_class=DEVICE_CLASS_EMPTY,
            icon="mdi:battery-high",
        ).extend({
            cv.Optional("min_value", default=1.0): cv.float_,
            cv.Optional("max_value", default=6553.5): cv.float_,
            cv.Optional("step", default=0.1): cv.float_,
        }),
        cv.Optional(CONF_CELL_REFERENCE_VOLTAGE): number.number_schema(
            DalyNumber,
            unit_of_measurement="mV",
            device_class=DEVICE_CLASS_VOLTAGE,
            icon="mdi:flash",
        ).extend({
            cv.Optional("min_value", default=1000): cv.int_,
            cv.Optional("max_value", default=5000): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        
        # Collect Board Settings
        cv.Optional(CONF_COLLECT_BOARDS_NUM): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_EMPTY,
            device_class=DEVICE_CLASS_EMPTY,
            icon="mdi:developer-board",
        ).extend({
            cv.Optional("min_value", default=0): cv.int_,
            cv.Optional("max_value", default=3): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_BOARD_1_CELL_NUM): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_EMPTY,
            device_class=DEVICE_CLASS_EMPTY,
            icon="mdi:battery-outline",
        ).extend({
            cv.Optional("min_value", default=0): cv.int_,
            cv.Optional("max_value", default=32): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_BOARD_2_CELL_NUM): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_EMPTY,
            device_class=DEVICE_CLASS_EMPTY,
            icon="mdi:battery-outline",
        ).extend({
            cv.Optional("min_value", default=0): cv.int_,
            cv.Optional("max_value", default=32): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_BOARD_3_CELL_NUM): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_EMPTY,
            device_class=DEVICE_CLASS_EMPTY,
            icon="mdi:battery-outline",
        ).extend({
            cv.Optional("min_value", default=0): cv.int_,
            cv.Optional("max_value", default=32): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_BOARD_1_TEMP_NUM): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_EMPTY,
            device_class=DEVICE_CLASS_EMPTY,
            icon="mdi:thermometer",
        ).extend({
            cv.Optional("min_value", default=0): cv.int_,
            cv.Optional("max_value", default=8): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_BOARD_2_TEMP_NUM): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_EMPTY,
            device_class=DEVICE_CLASS_EMPTY,
            icon="mdi:thermometer",
        ).extend({
            cv.Optional("min_value", default=0): cv.int_,
            cv.Optional("max_value", default=8): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_BOARD_3_TEMP_NUM): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_EMPTY,
            device_class=DEVICE_CLASS_EMPTY,
            icon="mdi:thermometer",
        ).extend({
            cv.Optional("min_value", default=0): cv.int_,
            cv.Optional("max_value", default=8): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        
        # Battery Type (0=LiFePO4, 1=Li-ion, 2=LTO)
        cv.Optional(CONF_BATTERY_TYPE): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_EMPTY,
            device_class=DEVICE_CLASS_EMPTY,
            icon="mdi:battery",
        ).extend({
            cv.Optional("min_value", default=0): cv.int_,
            cv.Optional("max_value", default=2): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        
        # Sleep Waiting Time
        cv.Optional(CONF_SLEEP_WAITING_TIME): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_SECOND,
            device_class=DEVICE_CLASS_EMPTY,
            icon="mdi:sleep",
        ).extend({
            cv.Optional("min_value", default=0): cv.int_,
            cv.Optional("max_value", default=65535): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        
        # Cell Voltage Protection Parameters (mV)
        cv.Optional(CONF_CELL_VOLTAGE_HIGH_WARNING): number.number_schema(
            DalyNumber,
            unit_of_measurement="mV",
            device_class=DEVICE_CLASS_VOLTAGE,
            icon="mdi:alert",
        ).extend({
            cv.Optional("min_value", default=1000): cv.int_,
            cv.Optional("max_value", default=5000): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_CELL_VOLTAGE_HIGH_CRITICAL): number.number_schema(
            DalyNumber,
            unit_of_measurement="mV",
            device_class=DEVICE_CLASS_VOLTAGE,
            icon="mdi:alert-octagon",
        ).extend({
            cv.Optional("min_value", default=1000): cv.int_,
            cv.Optional("max_value", default=5000): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_CELL_VOLTAGE_LOW_WARNING): number.number_schema(
            DalyNumber,
            unit_of_measurement="mV",
            device_class=DEVICE_CLASS_VOLTAGE,
            icon="mdi:alert",
        ).extend({
            cv.Optional("min_value", default=1000): cv.int_,
            cv.Optional("max_value", default=5000): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_CELL_VOLTAGE_LOW_CRITICAL): number.number_schema(
            DalyNumber,
            unit_of_measurement="mV",
            device_class=DEVICE_CLASS_VOLTAGE,
            icon="mdi:alert-octagon",
        ).extend({
            cv.Optional("min_value", default=1000): cv.int_,
            cv.Optional("max_value", default=5000): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        
        # Total Voltage Protection Parameters (0.1V)
        cv.Optional(CONF_TOTAL_VOLTAGE_HIGH_WARNING): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_VOLT,
            device_class=DEVICE_CLASS_VOLTAGE,
            icon="mdi:alert",
        ).extend({
            cv.Optional("min_value", default=1.0): cv.float_,
            cv.Optional("max_value", default=100.0): cv.float_,
            cv.Optional("step", default=0.1): cv.float_,
        }),
        cv.Optional(CONF_TOTAL_VOLTAGE_HIGH_CRITICAL): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_VOLT,
            device_class=DEVICE_CLASS_VOLTAGE,
            icon="mdi:alert-octagon",
        ).extend({
            cv.Optional("min_value", default=1.0): cv.float_,
            cv.Optional("max_value", default=100.0): cv.float_,
            cv.Optional("step", default=0.1): cv.float_,
        }),
        cv.Optional(CONF_TOTAL_VOLTAGE_LOW_WARNING): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_VOLT,
            device_class=DEVICE_CLASS_VOLTAGE,
            icon="mdi:alert",
        ).extend({
            cv.Optional("min_value", default=1.0): cv.float_,
            cv.Optional("max_value", default=100.0): cv.float_,
            cv.Optional("step", default=0.1): cv.float_,
        }),
        cv.Optional(CONF_TOTAL_VOLTAGE_LOW_CRITICAL): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_VOLT,
            device_class=DEVICE_CLASS_VOLTAGE,
            icon="mdi:alert-octagon",
        ).extend({
            cv.Optional("min_value", default=1.0): cv.float_,
            cv.Optional("max_value", default=100.0): cv.float_,
            cv.Optional("step", default=0.1): cv.float_,
        }),
        
        # Current Protection Parameters (0.1A, with 30000 offset - values already converted by user)
        cv.Optional(CONF_CHARGING_CURRENT_HIGH_WARNING): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_AMPERE,
            device_class=DEVICE_CLASS_CURRENT,
            icon="mdi:alert",
        ).extend({
            cv.Optional("min_value", default=-3000.0): cv.float_,
            cv.Optional("max_value", default=3553.5): cv.float_,
            cv.Optional("step", default=0.1): cv.float_,
        }),
        cv.Optional(CONF_CHARGING_CURRENT_HIGH_CRITICAL): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_AMPERE,
            device_class=DEVICE_CLASS_CURRENT,
            icon="mdi:alert-octagon",
        ).extend({
            cv.Optional("min_value", default=-3000.0): cv.float_,
            cv.Optional("max_value", default=3553.5): cv.float_,
            cv.Optional("step", default=0.1): cv.float_,
        }),
        cv.Optional(CONF_DISCHARGING_CURRENT_HIGH_WARNING): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_AMPERE,
            device_class=DEVICE_CLASS_CURRENT,
            icon="mdi:alert",
        ).extend({
            cv.Optional("min_value", default=-3000.0): cv.float_,
            cv.Optional("max_value", default=3553.5): cv.float_,
            cv.Optional("step", default=0.1): cv.float_,
        }),
        cv.Optional(CONF_DISCHARGING_CURRENT_HIGH_CRITICAL): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_AMPERE,
            device_class=DEVICE_CLASS_CURRENT,
            icon="mdi:alert-octagon",
        ).extend({
            cv.Optional("min_value", default=-3000.0): cv.float_,
            cv.Optional("max_value", default=3553.5): cv.float_,
            cv.Optional("step", default=0.1): cv.float_,
        }),
        
        # Temperature Protection Parameters (°C, with -40 offset - values already converted by user)
        cv.Optional(CONF_CHARGING_TEMP_HIGH_WARNING): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_CELSIUS,
            device_class=DEVICE_CLASS_TEMPERATURE,
            icon="mdi:alert",
        ).extend({
            cv.Optional("min_value", default=-40): cv.int_,
            cv.Optional("max_value", default=100): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_CHARGING_TEMP_HIGH_CRITICAL): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_CELSIUS,
            device_class=DEVICE_CLASS_TEMPERATURE,
            icon="mdi:alert-octagon",
        ).extend({
            cv.Optional("min_value", default=-40): cv.int_,
            cv.Optional("max_value", default=100): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_CHARGING_TEMP_LOW_WARNING): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_CELSIUS,
            device_class=DEVICE_CLASS_TEMPERATURE,
            icon="mdi:alert",
        ).extend({
            cv.Optional("min_value", default=-40): cv.int_,
            cv.Optional("max_value", default=100): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_CHARGING_TEMP_LOW_CRITICAL): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_CELSIUS,
            device_class=DEVICE_CLASS_TEMPERATURE,
            icon="mdi:alert-octagon",
        ).extend({
            cv.Optional("min_value", default=-40): cv.int_,
            cv.Optional("max_value", default=100): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_DISCHARGING_TEMP_HIGH_WARNING): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_CELSIUS,
            device_class=DEVICE_CLASS_TEMPERATURE,
            icon="mdi:alert",
        ).extend({
            cv.Optional("min_value", default=-40): cv.int_,
            cv.Optional("max_value", default=100): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_DISCHARGING_TEMP_HIGH_CRITICAL): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_CELSIUS,
            device_class=DEVICE_CLASS_TEMPERATURE,
            icon="mdi:alert-octagon",
        ).extend({
            cv.Optional("min_value", default=-40): cv.int_,
            cv.Optional("max_value", default=100): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_DISCHARGING_TEMP_LOW_WARNING): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_CELSIUS,
            device_class=DEVICE_CLASS_TEMPERATURE,
            icon="mdi:alert",
        ).extend({
            cv.Optional("min_value", default=-40): cv.int_,
            cv.Optional("max_value", default=100): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_DISCHARGING_TEMP_LOW_CRITICAL): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_CELSIUS,
            device_class=DEVICE_CLASS_TEMPERATURE,
            icon="mdi:alert-octagon",
        ).extend({
            cv.Optional("min_value", default=-40): cv.int_,
            cv.Optional("max_value", default=100): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        
        # Differential Protection Parameters
        cv.Optional(CONF_EXCESSIVE_VOLTAGE_DIFF_WARNING): number.number_schema(
            DalyNumber,
            unit_of_measurement="mV",
            device_class=DEVICE_CLASS_VOLTAGE,
            icon="mdi:alert",
        ).extend({
            cv.Optional("min_value", default=0): cv.int_,
            cv.Optional("max_value", default=1000): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_EXCESSIVE_VOLTAGE_DIFF_CRITICAL): number.number_schema(
            DalyNumber,
            unit_of_measurement="mV",
            device_class=DEVICE_CLASS_VOLTAGE,
            icon="mdi:alert-octagon",
        ).extend({
            cv.Optional("min_value", default=0): cv.int_,
            cv.Optional("max_value", default=1000): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_EXCESSIVE_TEMP_DIFF_WARNING): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_CELSIUS,
            device_class=DEVICE_CLASS_TEMPERATURE,
            icon="mdi:alert",
        ).extend({
            cv.Optional("min_value", default=0): cv.int_,
            cv.Optional("max_value", default=100): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_EXCESSIVE_TEMP_DIFF_CRITICAL): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_CELSIUS,
            device_class=DEVICE_CLASS_TEMPERATURE,
            icon="mdi:alert-octagon",
        ).extend({
            cv.Optional("min_value", default=0): cv.int_,
            cv.Optional("max_value", default=100): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        
        # Balancing Parameters
        cv.Optional(CONF_BALANCING_TURN_ON_VOLTAGE): number.number_schema(
            DalyNumber,
            unit_of_measurement="mV",
            device_class=DEVICE_CLASS_VOLTAGE,
            icon="mdi:scale-balance",
        ).extend({
            cv.Optional("min_value", default=1000): cv.int_,
            cv.Optional("max_value", default=5000): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        cv.Optional(CONF_BALANCING_VOLTAGE_DIFF): number.number_schema(
            DalyNumber,
            unit_of_measurement="mV",
            device_class=DEVICE_CLASS_VOLTAGE,
            icon="mdi:scale-balance",
        ).extend({
            cv.Optional("min_value", default=0): cv.int_,
            cv.Optional("max_value", default=500): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
        
        # SOC Setting
        cv.Optional(CONF_SOC_SETTING): number.number_schema(
            DalyNumber,
            unit_of_measurement="%",
            device_class=DEVICE_CLASS_EMPTY,
            icon="mdi:battery-50",
        ).extend({
            cv.Optional("min_value", default=0.0): cv.float_,
            cv.Optional("max_value", default=100.0): cv.float_,
            cv.Optional("step", default=0.1): cv.float_,
        }),
        
        # MOS Temperature Protection
        cv.Optional(CONF_MOS_TEMP_PROTECTION): number.number_schema(
            DalyNumber,
            unit_of_measurement=UNIT_CELSIUS,
            device_class=DEVICE_CLASS_TEMPERATURE,
            icon="mdi:chip",
        ).extend({
            cv.Optional("min_value", default=-40): cv.int_,
            cv.Optional("max_value", default=100): cv.int_,
            cv.Optional("step", default=1): cv.int_,
        }),
    }
)


async def to_code(config):
    hub = await cg.get_variable(config[CONF_DALY_BMS_BLE_ID])
    for key, address in NUMBERS.items():
        if key in config:
            conf = config[key]
            var = cg.new_Pvariable(conf[CONF_ID])
            await cg.register_component(var, conf)
            await number.register_number(var, conf, min_value=conf.get("min_value"), max_value=conf.get("max_value"), step=conf.get("step"))
            cg.add(getattr(hub, f"set_{key}_number")(var))
            cg.add(var.set_parent(hub))
            cg.add(var.set_holding_register(address))
