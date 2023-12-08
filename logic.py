from PyQt6.QtWidgets import *
from gui import *
import csv
import os


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        '''
        This function will initialize the ballot and
        will only show the items needed for the voter ID.
        It will also create the csv file.
        '''
        super().__init__()
        self.setupUi(self)
        self.push_submit.clicked.connect(lambda: self.submit())
        self.push_vote.clicked.connect(lambda: self.vote())
        self.push_next.clicked.connect(lambda: self.next())
        self.push_enter.clicked.connect(lambda: self.enter())
        self.push_end.clicked.connect(lambda: self.end())
        self.label_error.setHidden(True)
        self.label_exit.setHidden(True)
        self.label_id_error.setHidden(True)
        self.label_vote_candid.setHidden(True)
        self.push_next.setHidden(True)
        self.push_submit.setHidden(True)
        self.push_end.setHidden(True)
        self.push_vote.setHidden(True)
        self.radio_exit.setHidden(True)
        self.radio_jane.setHidden(True)
        self.radio_john.setHidden(True)
        self.radio_vote.setHidden(True)
        self.jane = 0
        self.john = 0
        self.list_of_read = []
        self.result = False
        self.voted_for = ''
        with open('voter_id.csv', 'w', newline='') as file:
            pass

    def enter(self) -> None:
        '''
        This function will check to make sure the ID is entered
        correctly. If the user has already voted, it will show who
        they voted for. Otherwise, it will take them to the next
        screen asking if they want to vote.
        '''
        self.label_id_error.setHidden(False)
        if len(self.input_id.text()) > 4 or len(self.input_id.text()) < 4 or self.input_id.text().isdigit() is False:
            self.label_id_error.setText("Please enter 4-digit number."
                                        "\nCheck for spaces.")
        else:
            with open('voter_id.csv', 'r') as readfile:
                read_file = csv.reader(readfile, delimiter=',')
                self.list_of_read = list(read_file)
                for row in self.list_of_read:
                    if self.input_id.text().split()[0] in row:
                        self.result = True
                        self.voted_for = row[1]
                if self.result is True:
                    self.label_exit.setHidden(False)
                    self.label_exit.setText(f"You've already voted for {self.voted_for}. Thank you!")
                    self.push_next.setHidden(False)
                    self.input_id.setHidden(True)
                    self.push_enter.setHidden(True)
                    self.label_id.setHidden(True)
                    self.label_id_error.setText("")
                    self.result = False
                else:
                    with open('voter_id.csv', 'a') as csvfile:
                        csv_file = csv.writer(csvfile)
                        csv_file.writerow([f'{self.input_id.text()}'])
                    self.push_enter.setHidden(True)
                    self.input_id.setHidden(True)
                    self.label_id.setHidden(True)
                    self.label_id_error.setHidden(True)
                    self.push_submit.setHidden(False)
                    self.label_vote_candid.setHidden(False)
                    self.label_vote_candid.setText("VOTER MENU")
                    self.radio_vote.setHidden(False)
                    self.radio_exit.setHidden(False)
                    self.radio_vote.setChecked(True)
                    self.radio_exit.setChecked(False)

    def submit(self) -> None:
        '''
        This function will check to see if the user chose to
        vote or exit. If the user chose to exit, it will go back
        to the initial screen. If the user chose to vote, it
        will go to the ballot.
        '''
        if self.radio_vote.isChecked():
            self.label_error.setHidden(True)
            self.label_vote_candid.setText("CANDIDATE MENU")
            self.radio_vote.setHidden(True)
            self.radio_exit.setHidden(True)
            self.radio_jane.setHidden(False)
            self.radio_john.setHidden(False)
            self.push_submit.setHidden(True)
            self.push_vote.setHidden(False)
        elif self.radio_exit.isChecked():
            self.label_error.setHidden(True)
            self.label_exit.setHidden(True)
            self.label_id_error.setHidden(True)
            self.label_vote_candid.setHidden(True)
            self.push_next.setHidden(True)
            self.push_submit.setHidden(True)
            self.push_vote.setHidden(True)
            self.radio_exit.setHidden(True)
            self.radio_jane.setHidden(True)
            self.radio_john.setHidden(True)
            self.radio_vote.setHidden(True)
            self.input_id.setHidden(False)
            self.label_id.setHidden(False)
            self.push_enter.setHidden(False)
            with open('voter_id.csv', 'r') as sourcefile:
                with open('result.csv', 'w') as resultfile:
                    csvwriter = csv.writer(resultfile)
                    csvreader = csv.reader(sourcefile)
                    for rows in csvreader:
                        if rows[0] == self.input_id.text():
                            pass
                        else:
                            csvwriter.writerow(rows)
            os.remove('voter_id.csv')
            os.rename('result.csv', 'voter_id.csv')
            self.input_id.setText("")

    def vote(self) -> None:
        '''
        This function will enter the vote for the user
        and add it to the csv file by matching the ID to
        the vote.
        '''
        if self.radio_jane.isChecked():
            self.jane += 1
            self.radio_jane.setHidden(True)
            self.radio_john.setHidden(True)
            self.push_vote.setHidden(True)
            self.push_next.setHidden(False)
            self.push_end.setHidden(False)
            self.label_error.setHidden(True)
            self.label_vote_candid.setHidden(True)
            with open('voter_id.csv', 'r') as sourcefile:
                with open('result.csv', 'w') as resultfile:
                    csvwriter = csv.writer(resultfile)
                    csvreader = csv.reader(sourcefile)
                    for rows in csvreader:
                        if rows[0] == self.input_id.text():
                            csvwriter.writerow([f'{self.input_id.text()}', 'Jane'])
                        else:
                            csvwriter.writerow(rows)
            os.remove('voter_id.csv')
            os.rename('result.csv', 'voter_id.csv')
        elif self.radio_john.isChecked():
            self.john += 1
            self.radio_jane.setHidden(True)
            self.radio_john.setHidden(True)
            self.push_vote.setHidden(True)
            self.push_next.setHidden(False)
            self.push_end.setHidden(False)
            self.label_error.setHidden(True)
            self.label_vote_candid.setHidden(True)
            with open('voter_id.csv', 'r') as sourcefile:
                with open('result.csv', 'w') as resultfile:
                    csvwriter = csv.writer(resultfile)
                    csvreader = csv.reader(sourcefile)
                    for rows in csvreader:
                        if rows[0] == self.input_id.text():
                            csvwriter.writerow([f'{self.input_id.text()}', 'John'])
                        else:
                            csvwriter.writerow(rows)
            os.remove('voter_id.csv')
            os.rename('result.csv', 'voter_id.csv')
        else:
            self.label_error.setHidden(False)
            self.label_error.setText("Please select an option.")

    def next(self) -> None:
        '''
        This function will take the user back to the
        initial screen to allow for the next voter.
        '''
        self.label_error.setHidden(True)
        self.label_exit.setHidden(True)
        self.label_id_error.setHidden(True)
        self.label_vote_candid.setHidden(True)
        self.push_next.setHidden(True)
        self.push_submit.setHidden(True)
        self.push_vote.setHidden(True)
        self.push_end.setHidden(True)
        self.radio_exit.setHidden(True)
        self.radio_jane.setHidden(True)
        self.radio_john.setHidden(True)
        self.radio_vote.setHidden(True)
        self.input_id.setText("")
        self.input_id.setHidden(False)
        self.label_id.setHidden(False)
        self.push_enter.setHidden(False)

    def end(self) -> None:
        '''
        This function ends the voting session, gives back
        a summary, and deletes the csv file for the next
        voting session.
        '''
        self.label_exit.setHidden(False)
        self.label_exit.setText("Thank you. Summary of the votes below:"
                                "\n---------------------------------------"
                                f"\nJane - {self.jane}, John - {self.john}, Total - {self.john + self.jane}"
                                "\n---------------------------------------")
        self.push_end.setHidden(True)
        self.push_next.setHidden(True)
        os.remove('voter_id.csv')
