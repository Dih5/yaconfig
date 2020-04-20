import yaconfig

metaconfig = yaconfig.MetaConfig(
    yaconfig.Variable("db", type=str, default="local.db", help="Database to use"),
    yaconfig.Variable("secret", type=bytes, default='_5#y2L"F4Q8z\n\xec]/', help="Flask secret"),
    # Note default values must be str. The are encoded to bytes using UTF8
    yaconfig.Variable("text", type=str, default="Ĉu vi komprenas tion?", help="Text to output")
)


# Get a default configuration, which should be overridden when the execution starts
config = yaconfig.Config(metaconfig)
