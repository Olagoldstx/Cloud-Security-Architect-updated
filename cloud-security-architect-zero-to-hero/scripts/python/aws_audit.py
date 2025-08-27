import boto3, json
iam = boto3.client("iam")
s3 = boto3.client("s3")
report = {"users_without_mfa": [], "public_buckets": []}

# Users without MFA
for u in iam.list_users()["Users"]:
    mfa = iam.list_mfa_devices(UserName=u["UserName"])["MFADevices"]
    if not mfa:
        report["users_without_mfa"].append(u["UserName"])

# Public buckets (basic check: ACL grants to AllUsers or AuthenticatedUsers)
for b in s3.list_buckets()["Buckets"]:
    name = b["Name"]
    try:
        acl = s3.get_bucket_acl(Bucket=name)
        for g in acl["Grants"]:
            uri = g.get("Grantee", {}).get("URI", "")
            if "AllUsers" in uri or "AuthenticatedUsers" in uri:
                report["public_buckets"].append(name)
                break
    except Exception as e:
        pass

print(json.dumps(report, indent=2))
