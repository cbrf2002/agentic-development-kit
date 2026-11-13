# Publication review

This kit contains original generic prompts and blank templates. It does not include project reports, client requirements, source code, keys, private network information, source SHAs or scanner evidence.

Before publishing a copy:

1. Choose repository visibility and a license. Verify ownership/permission for any added third-party material.
2. Run `python scripts/validate.py` and a full-history secret scan with a suitable tool. The validator is a structural check, not a secret scanner or security clearance.
3. Inspect staged files and archive contents. Ignore rules do not remove already tracked or historical secrets.
4. Keep restricted outputs outside the published tree. Use synthetic examples and explicit placeholders.
5. Remove local paths, account names, internal URLs and private evidence references introduced during adaptation.
6. Review tool licenses/entitlements before installing or using them in private projects. Do not assume a tool listed in a prompt is installed or permitted.

No external publication is performed by this kit. Initialize and publish the repository after reviewing its contents. Configure branch protection and review requirements for your hosting service.
