'''
Project list
'''

#define project as key-value pairs

def get_project(project):
    projects = {
        "signal-android" : "https://github.com/signalapp/Signal-Android",
        "telegram" : "https://github.com/DrKLO/Telegram",
        "k-9" : "https://github.com/k9mail/k-9",
        "opentasks" : "https://github.com/dmfs/opentasks",
        "tasks" : "https://github.com/tasks/tasks",
        "omni-notes" : "https://github.com/federicoiosue/Omni-Notes",
        "ncalc" : "https://github.com/tranleduy2000/ncalc",
        "calculator" : "https://github.com/Xlythe/Calculator"
    }

    return projects[project]
