# Expense-Tracker
it is simple expense tracker using python tkinter library which beginner friendly project for new python learners
here 
we connected  it to xxamp server

requirements 
vs code
xxamp

in xxamp 
start apache, mysql
then open mysql  admin which opens it phpmyadmin 
1.now create db name expense
2. open query section and run following query for creating table with required columns

query
CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount FLOAT,
    item_description VARCHAR(255),
    category VARCHAR(100),
    expense_date DATE
);
