group = data.get('group')
threshold_percentage = data.get('threshold', 70)

# Zugriff auf die Zustände aller Entitäten in der Gruppe
group_entities = hass.states.get(group).attributes['entity_id']
total_entities = len(group_entities)
on_entities = sum(1 for entity_id in group_entities if hass.states.get(entity_id).state == 'on')
off_entities = total_entities - on_entities

# Berechnung, ob mehr als threshold_percentage der Lichter eingeschaltet sind
on_percentage = (on_entities / total_entities) * 100

# Entscheidung, ob die Lichter ein- oder ausgeschaltet werden sollen
action_service = ""
if on_percentage > threshold_percentage:
    # Mehr als threshold_percentage sind eingeschaltet, schalte alle ein
    action_service = "homeassistant.turn_on"
elif on_percentage < (100 - threshold_percentage):
    # Weniger als threshold_percentage sind eingeschaltet, schalte alle aus
    action_service = "homeassistant.turn_off"

# Führe die Aktion aus, wenn eine Aktion bestimmt wurde
if action_service:
    for entity_id in group_entities:
        hass.services.call('homeassistant', action_service.split('.')[1], {'entity_id': entity_id}, False)
