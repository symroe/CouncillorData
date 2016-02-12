# Some hacky Modern.Gov API parsing stuff.

Modern.Gov exposes some APIs to the world on some Council installs.

The endpoints I've found are:

* CheckComms
* GetAllMeetingsByDate
* GetAttachment
* GetAttachmentByPath
* GetCalendarEvents
* GetCommittees
* GetCommitteesByUser
* GetCouncillorsByPostcode
* GetCouncillorsByWard
* GetCouncillorsByWardId
* GetDeletedWebcastMeetings
* GetElectionResults
* GetElectionResultsRdf
* GetMeeting
* GetMeetings
* GetMemberGroup
* GetMpOrMepAndWardsByPostcode
* GetMpOrMepsAndWards
* GetParishCouncils
* GetServerDiagnostics
* GetWebCastMeetings

and they are normally found at `[domain]/mgWebService.asmx/[endpoint_name]`.

There is all sorts of fun to be had with this data!

This repo is some hacking whilst talking to people at #NotWestminster.  It's really rough, and designed for getting some data out, not for being stable or even sensible.

## Domains

I found loads of installs of modern.gov by doing the following Google search:

> inurl:mgWebService inurl:gov

and copying and pasting the domains in to `urls.txt`

## Scraping

Run:

`python scrape_all.py`

And wait a while (not all URLs work at the moment)

## Councillor Photos!

To get some photos!:

```
python parse_photos.py > photo_urls.txt
mkdir photos
cd photos
while read -r url filename tail; do
  wget -O "$filename" "$url" || err=1
done <../photo_urls.txt
```
