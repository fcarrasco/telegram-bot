rules = [
    {
        'rules': ['bot.*funcionando', 'bot.*ligado'],
        'action_type': 'message',
        'actions': ['SIM', 'Sim', 'Yep', 'y']
    },
    {
        'rules': ['sticker'],
        'action_type': 'sticker',
        'actions': ['CAADAQADCwADR4jEBXhIwd95RlnsAg']
    },
    {
        'rules': ['/gif\s*(.*)'],
        'action_type': 'gif',
        'actions': []
    },
]
