from bs4 import BeautifulSoup
from glob import glob
from pathlib import Path
from typing import Literal

CONTENT_TYPE = Literal["text", "others"]


class Event:
    _raw: BeautifulSoup
    sender: str | None = None
    content_type: CONTENT_TYPE = "text"  # unused
    content: str = ""

    def __init__(self, soup: BeautifulSoup):
        self._raw = soup
        self._get_sender()
        self._get_content()

    def _get_sender(self) -> str | None:
        """Try to find `mx_DisambiguatedProfile` and extract sender info."""
        profile = self._raw.find(attrs={"class": "mx_DisambiguatedProfile"})
        self.sender = profile.text.lower() if profile != None else None
        return self.sender

    def _get_content(self) -> str:
        """Get the content of the event."""
        content_event = self._raw.find(attrs={"class": "mx_EventTile_content"})
        self.content = content_event.text if content_event != None else ""
        return self.content


class Counter:
    data = {"user1": {"I": 0, "YOU": 0}, "user0": {"I": 0, "YOU": 0}}

    def count(
        self,
        text: str,
        sender: str,
        count_as_you: dict = {"user1": "user0", "user0": "user1"},
    ) -> tuple[int, int]:
        I_count = text.count("我")
        YOU_count = text.count("你") + text.count(count_as_you[sender])
        return I_count, YOU_count

    def update(self, event: Event):
        if event.sender:
            I, YOU = self.count(event.content, event.sender)
            self.data[event.sender]["I"] += I
            self.data[event.sender]["YOU"] += YOU
        else:
            raise ValueError("Event Sender is None when counting")


def event_executor(event: Event, last_sender: str, counter: Counter) -> str:
    """Execute a series of operations for every event in a queue.

    1. Update the sender to last sender if current sender is None. Return the
        current event's sender.
    2. Word count.
    """
    if event.sender == None:
        event.sender = last_sender

    counter.update(event)

    return event.sender


def main():
    files = glob("data/**/*.html")
    sender = ""
    counter = Counter()
    for html_file in files:
        with Path(html_file).open("r") as f:
            text = f.read()
            soup = BeautifulSoup(text, features="html.parser")
            for event_soup in soup.find_all("div", class_="mx_Export_EventWrapper"):
                event = Event(event_soup)
                # This event is not a text message
                if event.content == "":
                    continue
                sender = event_executor(event, last_sender=sender, counter=counter)

    print(counter.data)


main()
