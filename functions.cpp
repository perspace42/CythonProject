#include "functions.h" //Assign the header file to the source code file 

//After having already determined that the tip value is a number, determine that the tip value conforms to the correct dolar amount
bool validateNumber(float tip){
    float roundedTip = int(tip * 100) / 100.0f; //Round to two decimal places
    return tip == roundedTip; //Return true if the number contains 0 to 2 decimal places
}