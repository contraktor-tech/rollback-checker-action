# Rollback Checker

This action checks if the commit message contains **rollback** or **revert**

Usage:

```yaml
- uses: contraktor-tech/rollback-checker-action@master
  id: rollback-checker

- run: |
  echo ${{ steps.rollback-checker.outputs.event }}
```

Outputs:

event: [ 'rollback', 'deploy']

when **rollback** or **revert** was in the commit message, event will return `'rollback'`

when not it will return `'deploy'`
