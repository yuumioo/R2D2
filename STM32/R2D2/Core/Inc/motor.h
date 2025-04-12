/*
 * motor.h
 *
 *  Created on: Apr 6, 2025
 *      Author: benja
 */
#include "main.h"
extern TIM_HandleTypeDef htim1;
#ifndef INC_MOTOR_H_
#define INC_MOTOR_H_

void IN_Forward(void);
void IN_Reverse(void);
void IN_Left(void);
void IN_Right(void);
void EN_Forward(uint16_t pwm_val);
void EN_Reverse(void);






#endif /* INC_MOTOR_H_ */
