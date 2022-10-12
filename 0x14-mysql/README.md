# MySQL
0. Install MySQL on both web-01 and web-02 servers.
1. Create a user and password for both MySQL databases which will allow the checker access to them.
2. In order to set up replication, There's need to have a database with at least one table and one row in primary MySQL server (web-01) to replicate from. Create a db and a table with atleast one entry. Make sure that holberton_user has SELECT permissions on your table so that we can check that the table exists and is not empty.
3. Before getting started with primary-replica synchronization, One more thing in place is needed. On primary MySQL server (web-01), create a new user the replica server.
4. Setup a Primary-Replica infrastructure using MySQL
5. Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.
