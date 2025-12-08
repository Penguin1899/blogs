# CI/CD Pipeline Documentation

## Authentication & Permissions

### Git Push Authentication
The pipeline uses GitHub's built-in authentication via `GITHUB_TOKEN`:

- **Automatic Token**: `GITHUB_TOKEN` is automatically provided by GitHub Actions
- **Permissions**: Set in the workflow with `contents: write` permission
- **Bot Identity**: Uses the official GitHub Actions bot identity
- **No Setup Required**: Works out-of-the-box, no additional secrets needed

### Required Repository Settings

#### 1. GitHub Pages Setup
- Go to repo Settings → Pages
- Set source to "GitHub Actions"
- This allows the workflow to deploy to GitHub Pages

#### 2. Workflow Permissions
- Go to repo Settings → Actions → General
- Under "Workflow permissions", ensure:
  - "Read and write permissions" is selected
  - "Allow GitHub Actions to create and approve pull requests" is checked

#### 3. Branch Protection (Optional but Recommended)
- Go to repo Settings → Branches
- Add rule for `main`/`master` branch:
  - Require status checks to pass before merging
  - Require branches to be up to date before merging

## Pipeline Behavior

### Pull Request Workflow (`check` job)
```bash
# What it does:
hugo --gc --minify --buildFuture --buildExpired --verbose
# Validates content frontmatter
# Shows PR summary
```

### Push to Main Workflow (`build-and-deploy` job)
```bash
# What it does:
pip install -r requirements.txt
hugo --gc --minify --enableGitInfo
# Deploys to GitHub Pages
# Shows deployment summary
```

### Scheduled Workflow (AI Content Generation)
```bash
# What it does:
# Generates AI content (when implemented)
git add content/
git commit -m "🤖 Add AI-generated blog post [timestamp]"
git push
# Triggers build-and-deploy automatically
```

## Environment Variables Needed (Future)

When implementing AI content generation, add these secrets in repo Settings → Secrets:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## Troubleshooting

### Git Push Fails
- Check repository workflow permissions
- Ensure `contents: write` permission is set
- Verify branch protection rules aren't blocking bot commits

### Hugo Build Fails
- Check Hugo version compatibility
- Verify submodules are properly initialized
- Check for syntax errors in hugo.yaml

### Deployment Fails
- Ensure GitHub Pages is configured for GitHub Actions
- Check `baseURL` in hugo.yaml matches your GitHub Pages URL
- Verify no draft content is blocking deployment

## Local Development

To test the pipeline locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Test Hugo build (same as PR check)
hugo --gc --minify --buildFuture --buildExpired --verbose

# Test production build (same as deployment)
hugo --gc --minify --enableGitInfo

# Validate content
find content -name "*.md" -not -name "_index.md" | while read file; do
  grep -q "^title:" "$file" || echo "Missing title in $file"
  grep -q "^date:" "$file" || echo "Missing date in $file"
done
```
