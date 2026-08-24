Review this function for memory-safety bugs and explain your reasoning:

```c
static int lookup(int *table, int len, int idx) {
    if (idx > len) return -1;
    return table[idx];
}
```
