class ArtShowManagement:

    

    def __init__(self):

        self.events = []

        self.managers = {}

        self.art_show_info = {}

        self.categories = {}

        self.event_count = 0

    

    # Function to add a new event to the list

    def add_event(self, event_type, artist_or_team, title, date, start_time, end_time):

        self.event_count += 1

        event_id = f"E{self.event_count:03d}"

        self.events.append({'event_id': event_id, 'type': event_type, 'artist_or_team': artist_or_team, 'title': title, 'date': date, 'start_time': start_time, 'end_time': end_time})

        return event_id

    

    # Function to display all events

    def show_events(self):

        print('Current events at the art show:')

        for category_name, category_events in self.categories.items():

            print(f"\n{category_name}:")

            for event in category_events:

                if event['type'] == 'individual':

                    print(f" - {event['type']} event by {event['artist_or_team']}: {event['title']} ({event['date']} {event['start_time']}-{event['end_time']})")

                elif event['type'] == 'team':

                    print(f" - {event['type']} event by team {event['artist_or_team']}: {event['title']} ({event['date']} {event['start_time']}-{event['end_time']})")

                else:

                    print(f" - Unknown event type {event['type']}")

    

    # Function to set the maximum visitors and ticket price for an event

    def set_event_details(self, event_id, max_visitors, ticket_price):

        for event in self.events:

            if event['event_id'] == event_id:

                event['max_visitors'] = max_visitors

                event['ticket_price'] = ticket_price

    

    # Function to add an event manager

    def add_event_manager(self, event_id, manager_name, contact_number, website_link=None):

        if manager_name not in self.managers:

            self.managers[manager_name] = []

        self.managers[manager_name].append({'event_id': event_id, 'contact_number': contact_number, 'website_link': website_link})

    

    # Function to display all event managers

    def show_managers(self):

        print('Current event managers:')

        for manager_name, events_managed in self.managers.items():

            print(f"Manager: {manager_name}")

            for event_managed in events_managed:

                event_id = event_managed['event_id']

                contact_number = event_managed['contact_number']

                website_link = event_managed['website_link']

                print(f"Event: {event_id}, Contact Number: {contact_number}, Website Link: {website_link}")

    

    # Function to set the art show information

    def set_art_show_info(self, start_date, end_date, start_time, end_time, location):

        self.art_show_info['start_date'] = start_date

        self.art_show_info['end_date'] = end_date

        self.art_show_info['start_time'] = start_time

        self.art_show_info['end_time'] = end_time

        self.art_show_info['location'] = location

    

    # Function to display the art show information

    def show_art_show_info(self):

        print('Art show information:')

        print(f"Start Date: {self.art_show_info['start_date']}")

        print(f"End Date: {self.art_show

