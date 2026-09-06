For an SSH/headless session, use Wrangler’s device login:

```bash
npx wrangler@latest login --device --browser=false
```

Wrangler prints a URL and a short code. Open the URL on your local computer or phone, enter the code, and approve access. Keep the SSH command running until it reports success.

Verify authentication with:

```bash
npx wrangler whoami
```

The `--device` option requires Wrangler **4.119.0 or later** and avoids the usual `localhost:8976` callback problem. For CI or unattended servers, use scoped `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` environment variables instead of interactive login. [Cloudflare Wrangler documentation](https://developers.cloudflare.com/workers/wrangler/commands/general/)