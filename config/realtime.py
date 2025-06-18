from core.util.functions.env import env

realtime_config = {
  "plugins": {
    
    "LocalStorage":       "core.realtime.plugins.LocalStorage",
    "Payload":            "core.realtime.plugins.Payload",
    "Service":            "core.realtime.plugins.Service",
    "ResourceEncryption": "core.realtime.plugins.ResourceEncryption",
    "UsageCalculator":    "core.realtime.plugins.UsageCalculator",

    ""

    "local_storage":      "core.realtime.plugins.LocalStorage",
    "payload":            "core.realtime.plugins.Payload",
    "service":            "core.realtime.plugins.Service",
    "encrypt":            "core.realtime.plugins.ResourceEncryption",
    "usage":              "core.realtime.plugins.UsageCalculator",


    # <<<< Do not remove this comment and below one >>>>
    # <<<< end plugins >>>>

    # Plugins enabled by default
    'default': [
      'local_storage',
      'payload',
      'service',
      'encrypt',
      'usage',
    ]
  },

  # 
  # Plugins Configuration
  # 

  # <<<< Do not remove this comment and below one >>>>
  # <<<< End File >>>>
}
