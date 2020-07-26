#include <cstdlib>
#include <iostream>
#include <string>
#include <array>
#include <string>
#include <set>
#include <ctime>
#include <vector>

#ifndef CLINIC_H
#define CLINIC_H

class Clinic {
private:
	std::string name;
	int currNumOfEmps;
	int max_clinicians;
	int ideal_clinicians;
	std::vector<std::string> min_staff; //A list of the bare minimum staff listed by Pediatric or Adult

public:
	Clinic();
	Clinic(std::string, std::vector<std::string>, int, int);
	void setName(std::string);
	void setMinStaff(std::vector<std::string>);
	void setMax(int);
	void setIdeal(int);
	void setCurrentEmps(int);

	std::string getName();
	std::vector<std::string> getMinStaff();
	int getMax();
	int getIdeal();
	int getCurrentEmps();
};

#endif
