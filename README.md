PostgreSQL Notes:

### Manual steps with `PGDATA` env variable unset:

Starting the server
run: `$ pg_ctl -D /usr/local/var/postgres start`
The path passed in with the `-D` flag is the "location of the database storage area" according to the help page from `$ pg_ctl --help`
On a Linux machine, this might stored at `/var/lib/pgsql/data`. 

Checking status of the server
Option 1: `$ ps aux | grep postgres`. You should see a group of postgres processes running

Option 2: `$ pg_ctl -D /usr/local/var/postgres status`. You will get a message that the server is running with the PID of the process.

Stopping the server
run: `$ pg_ctl -D /usr/local/var/postgres stop`



### Manual steps with `PGDATA` env variable set:

Note with the commands above you need to use the `-D` flag to specify the location of the database storage area. 
This is nice if we want to configure this, but we don't need to specify a different location so this is unnecessary. 

If we don't want to pass in the flag, we can set an environment variable called `PGDATA` that stores the path of the location. So for this example we would open up our `~/.bashrc` or `~/.bashprofile` and add a line:
```
export PGDATA='/usr_/local/var/postgres'
```
remember to source the file to make it take effect, `$ . ~/.bashrc`

Now we can run the commands above without passing in the path:

Start the server: `$ pg_ctl start`
Check the status: `$ pg_ctl status`
Stop the server: `$ pg_ctl stop`


### TLDR;
set the environment variable: `export PGDATA='/usr_/local/var/postgres'`
start the postgres server: `$ pg_ctl start`

Helpful links:
https://tableplus.io/blog/2018/10/how-to-start-stop-restart-postgresql-server.html
https://www.postgresql.org/docs/current/storage-file-layout.html
https://stackoverflow.com/questions/7975414/how-to-check-status-of-postgresql-server-mac-os-x

#### psql command line tips

change databases: `\c [db name]`
describe tables: `\dt`
describe a table: `\d [table name]`
