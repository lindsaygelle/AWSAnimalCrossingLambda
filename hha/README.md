# HHA
HHA

Happy Home Academy.

## Instructions

Set up `development` environment.

```bash
terraform workspace new development
```

Set up `production` environment.
```bash
terraform workspace new production
```

Select `development` environment.
```bash
terraform select development
```

Initialize terraform configuration.
```bash
terraform init -upgrade
```

Plan terraform configuration.
```bash
terraform plan
```
