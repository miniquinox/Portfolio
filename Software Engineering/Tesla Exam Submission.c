#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
 
////////////////////////////////////////////////////////////////////////////////
/* TESLA MOTORS FIRMWARE TEST
 * You have 120 minutes to complete the test. There are 100 points total.
 *
 * All solutions should compile in Coderpad.io without error or warnings
 *
 * Penalties:
 * -1 / minute over time
 * -3 for 1 or more compilation errors
 * -2 for 1 or more compilation warnings
 *
 * Do not use outside aid
 *
 * A main() function is provided at the bottom for your use
 */
////////////////////////////////////////////////////////////////////////////////
 
////////////////////////////////////////////////////////////////////////////////
// 1) Macro (10 points)
//    Create a macro (named C_TO_F) to convert from degrees Celsius to Fahrenheit
//    Macro should work for integer or floating point types
//    Note: degF = degC * (9/5) + 32
// Answer: DONE

#define C_TO_F(c) (9 * c) / 5 + 32



////////////////////////////////////////////////////////////////////////////////
// 2) Bit Manipulation (5 points)
//    Write a function that inverts (0 -> 1 or 1 -> 0) the most significant and
//    least significant bits of the data value pointed to by b.


 
void flip_hi_lo(uint8_t* b)
{
    // Answer: DONE
  
  *b = *b ^ 129;
}
 
////////////////////////////////////////////////////////////////////////////////
// 3) Debugging (5 points)
//    The function computeSquareADC() has not been producing correct
//    output consistently. Please describe all issues with the function.
// Answer: ADC_Result is a 8bit number, multiplying to itself will yield
// an 8 bit number which may have an overflow during multiplication. 
// Both ADC_RESULT should be cast to uint16_t before perform any operation.
 
volatile uint8_t ADC_RESULT;
uint8_t computeSquareADC(void)
{
    uint16_t retval = ADC_RESULT * ADC_RESULT;
    return retval;
}
 
////////////////////////////////////////////////////////////////////////////////
// 4) Memory dump (10 points)
//    The following memory dump was taken while debugging an issue.
//
// Memory Dump:
// Address:  Byte:
// 0x1000    0xA0
// 0x1001    0x0A
// 0x1002    0xBA
// 0x1003    0x48
// 0x1004    0x2C
// 0x1005    0xB7
// 0x1006    0x3B
// 0x1007    0x82
// 0x1008    0x9C
// 0x1009    0xE5
// 0x100A    0x17
// 0x100B    0x40
// 0x100C    0xEF
// 0x100D    0x47
// 0x100E    0x0F
// 0x100F    0x98
// 0x1010    0x6F
// 0x1011    0xD5
// 0x1012    0x70
// 0x1013    0x9E
// 0x1014    0x94
// 0x1015    0x99
// 0x1016    0x4A
// 0x1017    0xBA
// 0x1018    0xCA
// 0x1019    0xB2
// 0x101A    0x32
// 0x101B    0xE6
// 0x101C    0x8E
// 0x101D    0xB9
// 0x101E    0xC5
// 0x101F    0x2E
// 0x1020    0xC3
//
// System is 32-bit, little-endian.
// A variable called myPacket is of type packet_S (typedef below).
// (Default compiler options; unpacked, naturally aligned.)
// The address of myPacket is 0x1010.
//
typedef struct
{
    uint8_t count;
    uint16_t data[2];
    uint32_t timestamp;
} packet_S;
 
// a) What are the values of each member of myPacket?
// Answer: count = 0x6F, data[0] = 0xD5, data[1] = 0x70, timestamp = 0x4A99949E
 
// b) If the system was big-endian, what would the values of each member of
//    myPacket be?
// Answer: count = 0x6F, data[0] = 0xD5, data[1] = 0x70, timestamp = 0x9E94994A
 
////////////////////////////////////////////////////////////////////////////////
// 5) State Machine (20 points)
//
//    Complete the function below to implement the state machine shown in the
//    diagram below for an electronic gumball vending machine.
//     * The initial state of the state machine should be IDLE
//     * The function should output the current state of the state machine
//     * Unexpected or invalid input should not cause a state transition
//     * GENERIC_FAULT may be received in any state and should put the machine
//       into the FAULT state
//
//
//          COIN      +---------+
//   +--------------->|         |   BUTTON
//   |                |  READY  | ---------+       
//   |    COIN_RETURN |         |          |
//   |   +----------- +---------+          |
//   |   |                                 |
//   |   V                                 V
// +---------+                        +---------+
// |         |     VEND_COMPLETE      |         |
// |  IDLE   |<-----------------------| VENDING |
// |         |                        |         |
// +---------+                        +---------+
//
//                                 +---------+
//                                 |         |
//                GENERIC_FAULT    |  FAULT  |
//             +------------------>|         |
//                                 +---------+
//
 
typedef enum
{
    IDLE,
    READY,
    VENDING,
    FAULT
} state_E;
 
typedef enum
{
    COIN,
    COIN_RETURN,
    BUTTON,
    VEND_COMPLETE,
    GENERIC_FAULT
} input_E;
 
state_E stateMachine(state_E currentState, input_E input)
{
    // Answer: TODO
    switch (currentState)
    {
      case IDLE:
        switch(input)
        {
          case COIN:
            return READY;
          case GENERIC_FAULT:
            return FAULT;
          default:
            return IDLE;
        }
        break;
      case READY:
        switch (input)
        {
            case COIN_RETURN:
              return IDLE;
          case BUTTON:
            return VENDING;
          case GENERIC_FAULT:
            return FAULT;
          default:
            return READY;
        }
        break;
      case VENDING:
        switch (input)
        {
          case VEND_COMPLETE:
            return IDLE;
          case GENERIC_FAULT:
            return FAULT;
          default:
            return VENDING;
        }
        break;
        default:
        return FAULT;
    }
    return FAULT;
}
 
 
////////////////////////////////////////////////////////////////////////////////
// 6) Unit Testing (10 points)
//    Write a unit test for validatePointerAndData that exercises all code paths
//    and branch conditions
 
// @param dataPtr - int32_t pointer to data to be used
//
// @return TRUE if pointer is non-NULL, data value is positive, non-zero and not
//         equal to the sentinel value 0x7FFFFFFF, FALSE otherwise
//
bool validatePointerAndData(int32_t* dataPtr)
{
    bool status = false;
    if ((dataPtr != NULL) &&
        (*dataPtr > 0)    &&
        (*dataPtr != 0x7FFFFFFF))
    {
        status = true;
    }
    return status;
}
 
//
// @return TRUE if all tests pass, FALSE otherwise
//
bool test_validatePointerAndData(void)
{ 
    //Answer: TODO
    int32_t number = 0;
    int32_t* numberptr = NULL;
    if(validatePointerAndData(numberptr))
    {
      return false;
    }
    numberptr = &number;
    if(validatePointerAndData(numberptr))
    {
      return false;
    }
  number = -5;
  if(validatePointerAndData(numberptr))
    {
      return false;
    }
    number = 15;
    if(!validatePointerAndData(numberptr))
    {
      return false;
    }
    number = 0x7FFFFFFF;
    if(validatePointerAndData(numberptr))
    {
      return false;
    }
  return true;
  
}
 
 
////////////////////////////////////////////////////////////////////////////////
// 7) Low Pass Filter (10 points)
//    Implement a function that will be called at 10hz (every 100 ms) and returns
//    an exponentially weighted average. The latest sample is given 1/10 weighting
//    and previous filtered value a weighting of 9/10. The function should
//    initialize the filter to the first sample value received if it is the first
//    time the function has run.

    // Answer: TODO

float lowPassSamples_10hz(float sample)
{ 
  static bool i = false;
  static float previousSample = 0.0f;
    if (!i)
    {
      previousSample = sample;
      i = true;
    }
  else 
  {
    previousSample = 9 * previousSample / 10 + sample / 10;
  }
    return previousSample;
}
 
////////////////////////////////////////////////////////////////////////////////
// 8a) Buffer (20 points: 8a + 8b)
//     Create a function to push a char into a FIFO. The FIFO should be implemented
//     as a circular buffer of length 20. The FIFO will be used to cache the most
//     recent data from a data stream, therefore, drop the oldest value if the
//     buffer is full.

    // Answer: DONE

#define BUFFER_SIZE 20U
char fifoBuffer[BUFFER_SIZE];
void bufferPush_ISR(char data)
{
  int i = 0;
  for (i = BUFFER_SIZE - 2; i >= 0; i--)
  {
    fifoBuffer[i + 1] = fifoBuffer[i];
  }
  fifoBuffer[0] = data;

}
 
////////////////////////////////////////////////////////////////////////////////
// 8b) Create a function to print out and empty the data buffer.
//     Data should be printed in order from oldest to newest, active elements only.
 
    // Answer: DONE

void printAndEmptyBuffer(void)
{
  //disableInterrupts();
  int i = 0;
  for(i = BUFFER_SIZE - 1; i >= 0; i--)
  {
    if (fifoBuffer[i] != 0)
      printf("%c ", fifoBuffer[i]);
    fifoBuffer[i] = 0;
  }
  //enableInterrupts();

}
 
////////////////////////////////////////////////////////////////////////////////
// 8c) Interrupts (10 points)
//     The function bufferPush_ISR() will be called from an interrupt service
//     routine whenever new data is available to be buffered.
//     The function printAndEmptyBuffer() will be called from a periodic task.
//     The functions disableInterrupts() and enableInterrupts() are available
//     for disabling and enabling interrupts, respectively.
//
//     In your implementations of bufferPush_ISR() and printAndEmptyBuffer(),
//     determine whether or not it is necessary to disable/enable interrupts.
//     If so, add comments where the calls are necessary. If not required,
//     briefly comment why not.
//
// Answer: Interrupt is necessary to prevent the data being add to array while emptying it.
 
 
int main()
{
  //Question 1
  printf("Enter your number: ");
  float c;
  scanf("%f", &c);
  printf("%f celsius is equal to %f farenheight\n", c, C_TO_F(c));

  
  //Question 2
  uint8_t d = 126;
  uint8_t e = d;
  uint8_t* g = &e;
  flip_hi_lo(g);
  printf("%d is inverted to %d\n", d, e);
  
  //Question 6
  if(test_validatePointerAndData())
  {
    printf("success\n");
  }
  else
  {
    printf("fail\n");
  }

  return 0;
}
