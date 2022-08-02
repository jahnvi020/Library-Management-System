# A system to->
    Add new books.
    Delete existing books.
    Maintain records of book issued and returned.
    View all books along with thier status.

# To run the project execute these->
    pip install tk;
    pip install pillow;
    create database libmanagement;
    create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));
    create table books_issued(bid varchar(20) primary key, issuedto varchar(30));
