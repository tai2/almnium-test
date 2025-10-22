In a terminal

```
npm run start:appium 
```

In another terminal

```
export ALUMNIUM_LOG_LEVEL=debug
export ALUMNIUM_LOG_PATH=alumnium.log
export OPENAI_API_KEY=$OPENAI_API_KEY
#export ALUMNIUM_MODEL="anthropic"
#export ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY
poetry run python test.py
```