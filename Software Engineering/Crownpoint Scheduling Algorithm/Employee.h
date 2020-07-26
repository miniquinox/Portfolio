#include <cstdlib>
#include <iostream>
#include <string>
#include <array>
#include <string>
#include <set>
#include <ctime>
#include <vector>

#ifndef EMPLOYEE_H
#define EMPLOYEE_H

class Employee {


private:
	std::string name_;
	std::vector<std::string> availability_;
	std::string prefAge_;
	std::string license_;
	int hours_ = 80;
	std::string scheduleType_;


public:

	//Employee(const std::string&, const std::string&, int);
	void		setAvailability(std::string);
	void		setPrefAge(std::string);
	void		setName(std::string);
	void		setLicense(std::string);
	void		setHours(int);
	void		setScheduleType(std::string);
	std::vector<std::string> getAvailability();
	std::string getPrefAge();
	std::string getName();
	std::string getLicense();
	int			getHours();
	std::string getScheduleType();


};

#endif