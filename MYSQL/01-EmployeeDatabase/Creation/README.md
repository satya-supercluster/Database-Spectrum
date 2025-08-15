# Database Installation Commands

```bash
 
Get-Content employee.sql | mysql -u root -p

# Test installation
Get-Content test_employee_md5.sql | mysql -u root -p -t

# Load optional functions (after dataset installation)
Get-Content object.sql | mysql -u root -p
```
