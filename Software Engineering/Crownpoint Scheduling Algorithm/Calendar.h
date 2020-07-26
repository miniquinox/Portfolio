#pragma once
#include <cstdlib>
#include <iostream>
#include <string>
#include <array>
#include <string>
#include <set>
#include <ctime>
#include <vector>

#ifndef CALENDAR_H
#define CALENDAR_H

class Calendar {
private:
	int         monthNum_;
	int         yearNum_;
	int			numOfDays_;
	std::string dayName_;
	bool        leapYear_;
	std::string dNames_[7] = { "Sun","Mon","Tue","Wed","Thu","Fri","Sat" };
	int			nDays_[12] = { 31,28,31,30,
							   31,30,31,31,
							   30,31,30,31 }; // not leap year;

public:
	void        setMonthYearNum(int, int);
	int         getMonthNum();
	std::string getMonthName(int);
	int         getYearNum();
	void        setDayName(int);
	std::string getDayName();
	int         dayNumber(int, int, int);
	void		setnumOfDays(int);
	int         getnumOfDays();

	void        checkYear(int);
};

#endif