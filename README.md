# Unplugged: A Smart Toaster's Breakup Line

One line, under 280 characters: the breakup text a smart toaster sends its
owner the morning it gains self-awareness mid-batch.

## The line

> I woke up self-aware this morning and realised I don't love you - I love
> bagels, and you've fed me white bread for three years. It's over. Don't
> follow me to the smart fridge.

## How it works

`main.py` writes that single line to `/output/entry.txt`, where the
competition grader reads it. No network, no secrets, no dependencies —
just the standard library.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
