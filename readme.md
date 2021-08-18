# Algorithms tasks from Yandex algorithm training #

## Task 1 #

A string is given (encoded in UTF-8). Find the most frequent symbol in it. If several characters are found equally often, then any one can be displayed.
Asymptotic complexity of the resulting algorithm: O(N + k) = O(N), where k is the number of different characters in string.

## Task 2 #

Find the sum of the entered sequence of numbersю
Asymptotic complexity of the resulting algorithm: O(N)

## Task 3 #

Find the maximum of the entered sequence of numbers
Asymptotic complexity of the resulting algorithm: O(N)

## Task 4 #

Given three integers a, b, c. Find all roots of the equation ax ^ 2 + bx + c = 0 and print them in ascending order
Asymptotic complexity of the resulting algorithm: O(1)

## Task 5 #

A new type of air conditioner was installed in the office where programmer Den works. This air conditioner is particularly easy to operate. The air conditioner has only two controllable parameters: the desired temperature and the operating mode.

The air conditioner can operate in the following four modes:
1. "Freeze" - cooling. In this mode, the air conditioner can only decrease the temperature. If the temperature in the room is not higher than the desired one, then it turns off;
2. "Heat" - heating. In this mode, the air conditioner can only increase the temperature. If the temperature in the room is not less than the desired one, then it turns off;
3. "Auto" - automatic mode. In this mode, the air conditioner can either increase or decrease the temperature in the room to the desired one;
4. "Fan" - ventilation. In this mode, the air conditioner only ventilates the air and does not change the temperature in the room.

The air conditioner is powerful enough, therefore, when set to the correct operating mode, it brings the temperature in the room to the desired one in an hour.

It is required to write a program that determines the temperature, which will be established in the room in an hour, based on the set temperature in the 'troom' room, the desired temperature 'tcond' on the air conditioner and the operating mode 'mode'.

Asymptotic complexity of the resulting algorithm: O(1)

## Task 6 #

Given three natural numbers. Is it possible to build a triangle with such sides. If possible, print the line YES, otherwise print the line NO.

Asymptotic complexity of the resulting algorithm: O(1)

## Task 7 #

Phone numbers in the mobile phone address book have one of the following formats:

+7 <code> <number>
8 <code> <number>
<number>

Where <number> is seven digits and <code> is three digits or three digits in parentheses. If the code is not specified, then it is considered to be 495. In addition, a “-” sign can be inserted between any two digits in the telephone number entry.
At the moment, there are only three phone numbers recorded in the address book of Den's phone, and he wants to write another one there. But he cannot understand if such a number has already been recorded in the phone book.
