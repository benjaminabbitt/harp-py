# harp-py

*Pronounced "harpy"*

**H**uman **A**ppropriate **R**andom **P**hraselets

Pure Python implementation of harp - generate memorable, human-readable random names from adjectives and nouns.

```
swift-amber-falcon      quiet-silver-meadow     bold-crimson-thunder
```

## Usage

```python
import harp

harp.generate_name()  # "spirited-unexposed-gatherer"
harp.generate_name_with_options(components=2)  # "choosy-iguana"
harp.generate_name_with_options(components=4, separator="_")  # "bold_keen_swift_falcon"
```

## API

- `generate_name()` - 3 components (adjective-adjective-noun)
- `generate_name_with_options(components=3, max_element_length=None, separator="-")`
- `version()` - library version

## Word Lists

1,269 adjectives and 4,396 nouns = 5.6 million combinations using only familiar words.

Curated from [EFF Diceware](https://www.eff.org/dice) and classified using [Moby Project](https://en.wikipedia.org/wiki/Moby_Project).

## License

BSD-3-Clause

---

*Name credit: [AdamPIcode](https://old.reddit.com/user/AdamPIcode)*
