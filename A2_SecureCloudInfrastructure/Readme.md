## Audit AWS cloud account for security compliance
* Open the CloudShell and execute the following commands

## Enable Security Hub (automatic compliance check)
  ```
aws securityhub enable-security-hub --enable-default-standards
  ```
```
aws securityhub get-findings > findings.json
```

## View results
```
cat findings.json
```
This shows security findings (like missing MFA, open ports, unencrypted buckets, etc.).
