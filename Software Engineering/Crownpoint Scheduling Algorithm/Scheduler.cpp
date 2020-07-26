#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include <array>
#include <nlohmann/json.hpp>
#include <vector>
#include "Support/Employee.h"
#include "Support/Clinic.h"
#include "Support/Calendar.h"

using std::string;
using std::vector;
using json = nlohmann::json;

/* initialize clinics */
vector<Clinic> initClinics()
{
	vector<Clinic> clinic;
	Clinic chf("CHF", { "pediatric","adult" }, 5, 5);
	clinic.push_back(chf);
	Clinic ths("THS", { "pediatric","adult" }, 2, 3);
	clinic.push_back(ths);
	Clinic ppch("PPCH", { "pediatric","adult" }, 2, 3);
	clinic.push_back(ppch);

	return clinic;
}

//finds an available employee that can fill a specific role at a clinic
int findQualifiedEmpIndex(std::vector<Employee> &employees, string neededAgeGroup, int osize)
{
	int index = -1;
	//int check = 0;
	for (int i = 0; i < osize; i++)
	{
		string empPrefAge = employees[i].getPrefAge();
		if (neededAgeGroup == empPrefAge || empPrefAge == "family") { //If the employees role matches the needed role
			index = i; //saves their index
			i = osize; // gets us out of the loop
		}
	}
	if (index == -1) {
		throw std::invalid_argument("No employees left to fill this position!");
	}
	else {
		employees[index].setPrefAge("null"); //Marks them as unavailable now that they've been picked
	}
	return index;
}

//Creates objects for each employee, and reads all of their information into those objects
vector<Employee> initEmployee(json jread) {
	std::vector<Employee> emp;
	Employee newemp;

	int jsize = jread.size();
	json::iterator it;
	int i;

	// Read JSON attributes
	for (i = 0; i < jsize; i++) {
		// Set Name and Preferred Age
		emp.push_back(newemp);
		emp[i].setName(jread[i]["Name"].get<string>());
		emp[i].setPrefAge(jread[i]["Preferred Age"].get<string>());
		// Set Available Days
		it = jread[i]["Available Days"].begin();
		for (it = jread[i]["Available Days"].begin(); it != jread[i]["Available Days"].end(); it++) {
			emp[i].setAvailability(*it);
		}
	}
	return emp;
}
//Marks each employee as available or unavailable given their listed availability 
void removeAvailable(vector<Employee>& employees, string day)
{
	int size = employees.size();
	for (int i = 0; i < size; i++)
	{
		vector<string> availableDays = employees[i].getAvailability();
		vector<string>::iterator it;

		it = find(availableDays.begin(), availableDays.end(), day); //checks if the current day is lised on their availability
		if (it == availableDays.end())
			employees[i].setPrefAge("null"); //marks them unavailable if the current day isn't found
	}
}

//gets a list of all of the dates in the given month
vector<string> scheduleDates(Calendar c)
{
	string dayname;
	int month, year, daynum;
	string date, monthname;

	int numOfDays = c.getnumOfDays();
	//std::cout << numOfDays << std::endl;
	vector<string> allDates;
	for (int i = 0; i <= numOfDays; i++) {
		if (i == 0) {
			allDates.push_back(" ");
		}
		else {
			month = c.getMonthNum();
			year = c.getYearNum();
			c.setDayName(c.dayNumber(i, month, year));
			monthname = c.getMonthName(month);

			date = c.getDayName() + " " + std::to_string(i) + "-" + monthname + "-" + std::to_string(year);
			allDates.push_back(date);
		}
	}
	return allDates;
}


// Makes blank schedule with names at the top and dates on the left hand side
vector<vector<string>> createCalendar(vector<string> dates, vector<Employee> emp) {
	vector<vector<string>> calendar;
	vector<string> row;
	string empName;
	string date;

	for (int i = 0; i < dates.size(); i++) {
		row = {};
		for (int j = 0; j <= emp.size(); j++) {
			if (i == 0) {
				if (j == 0) {
					row.push_back("-X-");
				}
				else {
					// Make name row
					int empi = j - 1;
					empName = emp[empi].getName();
					row.push_back(empName);
				}
			}
			else {
				if (j == 0) {
					date = dates[i];
					row.push_back(date);
				}
				else {
					row.push_back(" ");
				}
			}
		}
		calendar.push_back(row);
	}
	return calendar;
}


// Makes the final schedule
vector<vector<string>> fillCalendar(vector<vector<string>> cal,vector<Employee> emp, vector<Clinic> cln, json jread) {
	string currDay, currDate, empName, currentEmpRole,clinicName = "";
	vector<string> minStaff;
	int empCount, empMax, empIdeal;
	int qindex;
	int currentEmpInd;
	vector<string>::iterator it;
	
	int nameIndex;
	int clinicIndex;
	int csize = cln.size();
	int empSize = emp.size();
	bool areMoreEmpAvailable = true;
	bool areMoreClinicsAvailable = true;

	for (int i = 1; i < cal.size(); i++) { // Rows
		currDate = cal[i][0];
		currDay = currDate.substr(0, 3);
		
			if (currDay != "Sun" && currDay != "Sat") { // checks if it's the weekend
				removeAvailable(emp,currDay);
				areMoreEmpAvailable = true;
				areMoreClinicsAvailable = true;
				while (areMoreEmpAvailable)
				{
					for (int j = 0; j < emp.size(); j++) // checks if more employees to schedule
					{
						currentEmpRole = emp[j].getPrefAge();
						empName = emp[j].getName();
						currentEmpInd = j;
						if (currentEmpRole != "null")
						{
							j = emp.size();
							areMoreEmpAvailable = true;
						}
						else if(j==emp.size())
						{
							areMoreEmpAvailable = false;
						}

					}
					if (areMoreEmpAvailable && !areMoreClinicsAvailable) //if minimum clinic capacity has been met, but more employees still need to be scheduled
					{
						int numOfFullClinics = 0;
						it = find(cal[0].begin(), cal[0].end(), empName);
						nameIndex = it - cal[0].begin();

						for (int c = 0; c < csize; c++) { //loops through clinics
							empCount = cln[c].getCurrentEmps();
							empMax = cln[c].getMax();
							if (empCount < empMax) //if current clinic hasn't reached max capacity
							{	//schedule employee at this clinic
								emp[currentEmpInd].setPrefAge("null");

								clinicName = cln[c].getName(); //fills the cell on the day (i) and under their name with the name of the clinic
								cal[i][nameIndex] = clinicName;  //
								empCount = cln[c].getCurrentEmps() + 1; //increment the current employee count of that clinic
								cln[c].setCurrentEmps(empCount);
								
								c = csize;
							}
							else
							{
								numOfFullClinics++; //increment the number of full clinics
							}
							if (numOfFullClinics == csize) //if all clinics are full
							{
								emp[currentEmpInd].setPrefAge("null");
								areMoreEmpAvailable = false; //Stop scheduling for today
							}
						}
					}
					else
					{
						while (areMoreClinicsAvailable) //While any clinics still need their minimum requirements met
						{
							for (int p = 0; p < csize; p++) //loops thru clinics
							{
								vector<string> availableClinic = cln[p].getMinStaff();
								if (!availableClinic.empty()) //if there are roles that need to be filled at current clinic
								{
									p = csize; //jumps out of loop
									areMoreClinicsAvailable = true;
								}
								else
								{
									areMoreClinicsAvailable = false; //all minimum requirements have been met
								}
							}
							for (int k = 0; k < csize; k++) { //Fill all clinics min requirements
								minStaff = cln[k].getMinStaff();
								while (!minStaff.empty())
								{
									clinicName = cln[k].getName(); //gets clinic name

									int minStaffSize = minStaff.size() - 1;
									string neededRole = minStaff[minStaffSize]; //gets role that needs to be filled
									qindex = findQualifiedEmpIndex(emp, neededRole, empSize); //check which employee can fill that role
									empName = emp[qindex].getName(); //gets the name of that employee
									it = find(cal[0].begin(), cal[0].end(), empName); //finds that employee on the schedule
									nameIndex = it - cal[0].begin();
									cal[i][nameIndex] = clinicName; //fills the cell on the day (i) and under their name with the name of the clinic
									minStaff.pop_back(); //removes the now fulfilled role from the clinic's list of required roles
									empCount = cln[k].getCurrentEmps() + 1; //increments the current employee count of that clinic
									cln[k].setCurrentEmps(empCount); 
									emp[qindex].setPrefAge("null"); //marks them unavailable
								}
								cln[k].setMinStaff({}); //that clinic's minimum requirements are filled

							}
						}
					}
				}
			}
			emp = initEmployee(jread);
			cln = initClinics();		
	}
	return cal;
}

//prints the schedule into a csv file
void printCSV(vector<vector<string>> calendar) {
	
	int rowsize = calendar.size();
	int colsize = calendar[0].size();

	std::ofstream myfile;
	myfile.open("CSV_test.csv");

	for (int i = 0; i < rowsize; i++) {
		for (int j = 0; j < colsize; j++) {
			myfile << calendar[i][j];
			myfile << ",";
		}
		myfile << "\n";
	}
	myfile.close();
}


/* Main function */

int main() {
	int jsize, i, m, y;
	json jread;
	Calendar cal;
	vector<Clinic> clinic;
	vector<string> vect;
	vector<Employee> enew;

	// User input for month and year
	std::cout << "Enter month #: ";
	std::cin >> m;
	std::cout << "Enter Year #: ";
	std::cin >> y;
	cal.setMonthYearNum(m,y);
	
	// Reading JSON
	std::ifstream jfile("User.json");
	jfile >> jread;
	
	// Initialize Employee and Clinic Classes
	enew = initEmployee(jread);
	clinic = initClinics();


	// 1. Scheduling dates
	vector<string> dates;
	dates = scheduleDates(cal);

	// 2. Create calendar
	vector<vector<string>> calendar;
	calendar = createCalendar(dates, enew);

	// 3. Fill calendar
	vector<vector<string>> fullCalendar;
	fullCalendar = fillCalendar(calendar,enew,clinic,jread);

	// 4. create csv
	printCSV(fullCalendar);

	return 0;
}
