import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


class Artist(models.Model):
    ArtistName = models.CharField(max_length=200,default='')
    def __str__(self):
        return self.ArtistName



class Album(models.Model):
    RecordingArtistID = models.ForeignKey(Artist, on_delete=models.CASCADE,default='')
    AlbumTitle = models.CharField(max_length=200, default='')
    RecordingLabel = models.CharField(max_length=200, default='')
    YearReleased = models.CharField(max_length=200, default='')
    NumberofTracks = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.AlbumTitle


class Albumtracks(models.Model):
    AlbumID  = models.ForeignKey(Album, on_delete=models.CASCADE,default='')
    TrackNumber = models.CharField(max_length=200, default='')
    TrackTitle = models.CharField(max_length=200, default='')
    TrackLenght = models.CharField(max_length=200, default='')
    def __str__(self):
        return '{}  :  {}'.format(self.AlbumID, self.TrackTitle)

class Albumgenre(models.Model):
    AlbumID  = models.ForeignKey(Album, on_delete=models.CASCADE,default='')
    Genre = models.CharField(max_length=200, default='')
    def __str__(self):
        return '{}  :  {}'.format(self.AlbumID, self.Genre)



class Recorded(models.Model):
    AlbumID = models.OneToOneField(Album,on_delete=models.CASCADE,primary_key=True,)
    Startdate = models.DateField('Started')
    Enddate = models.DateField('Finished')
    def __str__(self):
        return '{} :   {} ---- {}'.format(self.AlbumID,self.Startdate,self.Enddate )

class Members(models.Model):
    RecordingArtistID = models.ForeignKey(Artist, on_delete=models.CASCADE,default='')
    Birthname = models.CharField(max_length=200, default='')
    Born =  models.DateField('Born')
    def __str__(self):
        return '{}  :  {}'.format(self.RecordingArtistID, self.Birthname)

class Instruments(models.Model):
    member = models.ForeignKey(Members, on_delete=models.CASCADE,default='')
    Instrument = models.CharField(max_length=200, default='')
    def __str__(self):
        return '{}  :  {}'.format(self.member, self.Instrument)

class Singles(models.Model):
    RecordingArtistID = models.ForeignKey(Artist, on_delete=models.CASCADE,default='')
    AlbumID = models.ForeignKey(Album, on_delete=models.CASCADE,blank=True,null=True,default='')
    Single = models.CharField(max_length=200, default='')
    Year = models.DateField('Year')
    def __str__(self):
        return '{}  :  {}'.format(self.RecordingArtistID, self.Single)

