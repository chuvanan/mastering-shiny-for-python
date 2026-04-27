
# Install driver (for Linux machine)

```bash
sudo apt-install unixodbc

# download package to configure MS repo
curl -sSL -O https://packages.microsoft.com/config/ubuntu/$(grep VERSION_ID /etc/os-release | cut -d '"' -f 2)/packages-microsoft-prod.deb

# install the package
sudo dpkg -i packages-microsoft-prod.deb

# install the driver
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18
```


Source: [MS ODBC 18](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16&tabs=ubuntu18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline#microsoft-odbc-18)

# Start docker container for SQL Server

```bash
sudo docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=1q2w3e&R" -p 1433:1433 --name sql5 -d mcr.microsoft.com/mssql/server:latest
```