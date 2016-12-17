from django.contrib import admin

from .models import Artist
from .models import Album
from .models import Albumtracks
from .models import Albumgenre
from .models import Recorded
from .models import Members
from .models import Instruments
from .models import Singles





class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id','ArtistName')
    list_display_links = ('id', 'ArtistName')
    search_fields = ('ArtistName',)
    list_filter = ("ArtistName",)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id','RecordingArtistID',"AlbumTitle","RecordingLabel","YearReleased","NumberofTracks")
    search_fields = ('RecordingArtistID__ArtistName',"AlbumTitle","RecordingLabel","YearReleased","NumberofTracks",)
    list_filter = ('RecordingArtistID__ArtistName',"AlbumTitle","RecordingLabel","RecordingLabel","YearReleased","NumberofTracks")

class AlbumtracksAdmin(admin.ModelAdmin):
    list_display = ('id','get_artist','get_album',"TrackNumber","TrackTitle","TrackLenght")
    search_fields = ('AlbumID__RecordingArtistID__ArtistName',"TrackNumber","TrackTitle","TrackLenght",)
    list_filter = ("TrackNumber", "TrackTitle", "TrackLenght",'AlbumID__RecordingArtistID__ArtistName')
    def get_artist(self, obj):
        return obj.AlbumID.RecordingArtistID.ArtistName
    def get_album(self, obj):
        return obj.AlbumID.AlbumTitle


class AlbumgenreAdmin(admin.ModelAdmin):
    list_display = ('id','get_artist','get_album',"Genre")
    search_fields = ("Genre",'AlbumID__RecordingArtistID__ArtistName','AlbumID__AlbumTitle')
    list_filter =  ("Genre",'AlbumID__RecordingArtistID__ArtistName','AlbumID__AlbumTitle')
    def get_album(self, obj):
        return obj.AlbumID.AlbumTitle
    def get_artist(self, obj):
        return obj.AlbumID.RecordingArtistID.ArtistName

class RecordedAdmin(admin.ModelAdmin):
    list_display = ('get_artist','get_album',"Startdate","Enddate")
    search_fields = ("Startdate","Enddate",'AlbumID__AlbumTitle',)
    list_filter = ("Startdate", "Enddate", 'AlbumID__AlbumTitle',)
    def get_album(self, obj):
        return obj.AlbumID.AlbumTitle
    def get_artist(self, obj):
        return obj.AlbumID.RecordingArtistID.ArtistName

class MembersAdmin(admin.ModelAdmin):
    list_display = ('id','RecordingArtistID',"Birthname","Born")
    search_fields = ("Birthname", "Born",'RecordingArtistID__ArtistName')
    list_filter = ("Birthname", "Born", 'RecordingArtistID__ArtistName')


class InstrumentsAdmin(admin.ModelAdmin):
    list_display = ('id',"get_artist","get_member","Instrument")
    search_fields = ("Instrument",'member__Birthname',"member__RecordingArtistID__ArtistName")
    list_filter = ("Instrument", 'member__Birthname', "member__RecordingArtistID__ArtistName")
    def get_artist(self, obj):
        return obj.member.RecordingArtistID.ArtistName
    def get_member(self, obj):
        return obj.member.Birthname

class SinglesAdmin(admin.ModelAdmin):
    list_display = ('id','RecordingArtistID',"AlbumID","Single","Year")
    search_fields = ("AlbumID__AlbumTitle","Single","Year","RecordingArtistID__ArtistName")
    list_filter = ("AlbumID__AlbumTitle", "Single", "Year", "RecordingArtistID__ArtistName")




admin.site.register(Artist,ArtistAdmin)
admin.site.register(Album,AlbumAdmin)
admin.site.register(Albumtracks,AlbumtracksAdmin)
admin.site.register(Albumgenre,AlbumgenreAdmin)
admin.site.register(Recorded,RecordedAdmin)
admin.site.register(Members,MembersAdmin)
admin.site.register(Instruments,InstrumentsAdmin)
admin.site.register(Singles,SinglesAdmin)







class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id','RecordingArtistID',"AlbumTitle","RecordingLabel","YearReleased","NumberofTracks")
    search_fields = ("AlbumTitle","RecordingLabel","YearReleased","NumberofTracks",)
    list_filter = ("AlbumTitle","RecordingLabel","YearReleased","NumberofTracks")









