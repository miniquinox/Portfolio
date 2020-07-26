#include "Calendar.h"
#include <iostream>
#include <iomanip>
#include <string>
#include <array>
#include <fstream>

using namespace std;

void Calendar::setMonthYearNum(int month, int year) {
	if (month < 1 || month > 12) {
		cout << "Invalid month. Set to Jan by default." << endl;
		monthNum_ = 1;
	}
	else {
		monthNum_ = month;
	}

	if (year < 2020) {
		cout << "Past years are invalid. Current year set by default." << endl;
		yearNum_ = 2020;
		checkYear(2020);
	}
	else {
		yearNum_ = year;
		checkYear(year);
	}

	setnumOfDays(monthNum_);
}

void Calendar::checkYear(int year) {
	if (year % 400 == 0 || year % 4 == 0) {
		nDays_[1] = 29;
	}
	else if (year % 100 == 0) {
		nDays_[1] = 28;
	}
	else {
		nDays_[1] = 28;
	}
}

int Calendar::getYearNum() {
	return yearNum_;
}

int Calendar::getMonthNum() {
	return monthNum_;
}

string Calendar::getMonthName(int monthNum) {
	string months[] = { "Jan","Feb","Mar","Apr",
						"May","Jun","Jul","Aug",
						"Sep","Oct","Nov","Dec" };
	return (months[monthNum - 1]);
}

void Calendar::setDayName(int day) {
	// index 0
	dayName_ = dNames_[day];
}

string Calendar::getDayName() {
	return dayName_;
}

int Calendar::dayNumber(int day, int month, int year) {
	static int t[] = { 0,3,2,5,0,3,5,1,4,6,2,4 };
	year -= month < 3;
	return (year + year / 4 - year / 100 + year / 400 + t[month - 1] + day) % 7;
}

void Calendar::setnumOfDays(int monthnum) {
	numOfDays_ = nDays_[monthnum - 1];
}

int Calendar::getnumOfDays() {
	return numOfDays_;
}
