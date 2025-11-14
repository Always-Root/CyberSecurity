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


## Apply IAM policies and set up multi-region backups for data redundancy on AWS.
* Open Open IAM Dashboard
* Create an IAM Group With Least-Privilege Policy
* Create an additional policy that requires MFA, improving account security.

Choose "JSON" and paste:
```
{
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "BoolIfExists": {
          "aws:MultiFactorAuthPresent": "false"
        }
      }
    }
  ]
}
```
* Attach to All IAM users

# S3 Multi-Region Backups for data redundancy
* Create S3 bucket for each location from where you want to backup and select that region for it.
* Go to Management tab and Find Replication rules
* Click Create rule and choose the following:
  
Source: Entire bucket
Destination: company-data-backup 
Enable Replicate delete markers
Click Save

* The data will be backup the selected destination(S3 bucket).
