#include "esphome/components/text_sensor/text_sensor.h"
#include "esphome/components/number/number.h"

// Other content of the file

// Method declarations

void request_settings();

// Member variables
uint32_t last_settings_request_ = 0;

// ... other code ...

// Add the setter methods after line 93

void set_rated_capacity_number(float value) {
  rated_capacity_number_->publish_state(value);
}

void set_cell_reference_voltage_number(float value) {
  cell_reference_voltage_number_->publish_state(value);
}

// 33 more setters follow...

void publish_state_(number::Number *number, float value) {
  number->publish_state(value);
}

// Define member variables after line 127
number::Number *rated_capacity_number_ = nullptr;
number::Number *cell_reference_voltage_number_ = nullptr;
// 33 more number pointers...

// End of file content.