# It's In, If
20 points

## Challenge 
> My older brother sent me [this photo](itsinif.8f2056d643d8.jpg), but I don’t know what to make of it.

## Hint
> What might big brother know?

## Solution

Strings

	$ strings itsinif.8f2056d643d8.jpg
	
	JFIF
	Exif
	NO CODE EXECUTION ALLOWED HERE
	PACTF
	Ihttp://ns.adobe.com/xap/1.0/
	<?xpacket begin='
	' id='W5M0MpCehiHzreSzNTczkc9d'?>
	<x:xmpmeta xmlns:x='adobe:ns:meta/' x:xmptk='Image::ExifTool 10.40'>
	<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
	 <rdf:Description rdf:about=''
	  xmlns:GPano='http://ns.google.com/photos/1.0/panorama/'>
	  <GPano:StitchingSoftware>big_brother_is_looking_at_your_photos</GPano:StitchingSoftware>
	 </rdf:Description>
	</rdf:RDF>
	</x:xmpmeta>


## Flag

	big_brother_is_looking_at_your_photos