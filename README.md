# folder-orderer

Step-by-step Streaming

Using streaming media files is as easy as browsing the Web, but there's a lot that goes on behind the scenes to make the process possible:
1.	Using your Web browser, you find a site that features streaming video or audio.
2.	You find the file you want to access, and you click the image, link or embedded player with your mouse.
3.	The Web server hosting the Web page requests the file from the streaming server.
4.	The software on the streaming server breaks the file into pieces and sends them to your computer using real-time protocols.
5.	The browser plugin, standalone player or Flash application on your computer decodes and displays the data as it arrives.
6.	Your computer discards the data.

Creating and distributing a streaming video or audio file requires its own process:
1.	You record a high-quality video or audio file using film or a digital recorder.
2.	You digitize this data by importing it to your computer and, if necessary, converting it with editing software.
3.	If you're creating a streaming video, you make the image size smaller and reduce the frame rate.
4.	A codec on your computer compresses the file and encodes it to the right format.
5.	You upload the file to a server
6.	The server streams the file to users' computers.


Most Popular Formats, Codecs and Containers 

First we need to understand what a video format is.
Usually people refer to the file’s extension as the video file’s format, but this isn’t
entirely correct. Some formats consist as a combination of files, folders and even playlists, all of which are needed to play the video properly.
To better understand video formats, let’s take a look at one specific video file and
understand how all of it’s parts work together to display the videos you see on your screen.
The file extension is actually a representation of what’s called the Container.
A Container for a video file is the part that contains all of the other files needed to
play back a specific video.
These files include the video stream, the audio stream, and the meta data.
This works with the video stream telling the player what needs to appear on the screen
while the audio stream tells the player which sounds needs to be played alongside the video.
The meta data, which means “data about data”, includes all of the other information about
the video, including things like the bit-rate type, resolution, subtitles, device and time
of creation, and more.

Codecs
One of the most important pieces of meta data is the codec.
The word codec is a combination of the words, coder and decoder.
As the title suggests it creates an encoded video or audio stream, making it smaller and
easier to manage. The player or target software then decodes it based on the rules set by that codec, and plays back the video with similar quality to the original.
Just like containers, there are hundreds of different codecs used on various audio and
video files.
Let’s cover the most important codecs for you to use, as well as their advantages and
disadvantages.
Let’s start with the video codecs.
A good place to begin is H.264, or AVC as it’s commonly referred to.
H.264 is by far the most commonly used video codec, mostly because it provides a significantly
better bitrate over it’s predecessors for the same file size. Video bitrate defines video data transferred at any given time. A high bitrate is doubtlessly one of the most crucial factors in the quality of a video.
For this reason, it is very widely supported and you can be confident you will rarely run
into any support issues using the H.264.
It’s successor, H.265 is referred to as HEVC which stands for High Efficiency Video
Coding. This codec delivers on it’s name, with a compression rate that is almost double that
of H.264. This means a file encoded with HEVC is going to be at least 50% smaller than a file
encoded in AVC. This is extremely beneficial for resolutions above 2k as well as video streaming.
The flip side of HEVC is that it’s much more complicated to encode, requiring triple
the resources for the video to be prepared for playback.
Adoption of HEVC is growing, after 3 years it’s still not nearly as popular
it’s predecessor. Apple has recently announced that they will support HEVC video, however there are some new codecs on the rise which give doubts as to whether it will become dominant.
For example, VP9 was developed by Google to be a royalty free and open source codec.
Originally it was used for YouTube, because it also increased bitrate 50% more that it’s
predecessor, VP8. Just like H.265, it’s good for high resolutions and live streaming, but is harder to decode and less supported than H.264. However, the technology behind VP9 generally makes streams more consistent and reliable, while H.265 usually provides a better overall image quality.
We just covered the main video codecs you need to think about, but audio codecs are
a different story and also very important for a clear understanding of streaming.
Let’s take a look at some of the most popular codecs for audio.
MP3 is one of the most famous audio codecs out there.
Developed by the Moving Pictures Experts Group in 1993, this lossy audio codec takes advantage of the limitations of human hearing, often referred to as auditory masking.
An example of this is that an MP3 often is reduced to 128 kbs, which sounds almost like
the original CD but is only 9% of the size.
24 years later, MP3 continues to be a popular format for sharing and playing back audio
content, but it has limited functionality for video and there are a few other audio
codecs that have become increasingly popular over the years.
For example AAC, which stands for Advanced Audio Coding, is a proprietary audio codec
developed shortly after MP3.
The main benefits of AAC are that it’s widely supported and that you get better sound for
the same bitrate. These reasons had made AAC the most popular codec to use for videos today.
There are little support issues and most of the time the is the best codec to use for
your video, however AAC does have a limit on audio channels, which means we will need
another codec to handle more robust video experiences.
If you need surround sound or backwards compatibility with Dolby products, AC3 may be the codec for you as it has a full range of channels, allowing it to fully preserve surround sound
settings. But aside from DVD players and digital television, AC3 doesn’t have nearly the device support of AAC.
There are other codecs as well, but currently those are the most important for audio and
video.

FFmpeg
FFmpeg is a free and open-source software project consisting of a large suite of libraries and programs for handling video, audio, and other multimedia files and streams. At its core is the FFmpeg program itself, designed for command-line-based processing of video and audio files. It is widely used for format transcoding, basic editing (trimming and concatenation), video scaling, video post-production effects and standards compliance (SMPTE, ITU).
FFmpeg includes libavcodec, an audio/video codec library used by many commercial and free software products, libavformat (Lavf),[7] an audio/video container mux and demux library, and the core ffmpeg command-line program for transcoding multimedia files.


Video File Formats
Now that we know the basics, we can finally talk about video file formats.
File Formats are standardized rules for storing the containers, codecs, meta data and sometimes
even folder structure of video files, so that it’s easier to support them across a large
number of different devices and players. Let’s talk about which video formats are most popular today and which formats are best to use in certain situations.

MP4
That first format we’ll look at is MP4, more specifically MPEG-4, and even more specifically
MPEG-4 Part 14.
The name MPEG-4 can be very confusing because different people use it for dozens of completely different things.
The three most common things people mean when they say MPEG-4 are:
The MP4 Container (MPEG-4 Part 14), which we are currently discussing
The ISO Base Media File Format (MPEG-4 Part 12) used for video streams.
The H.264 codec (MPEG-4 Part 10) is used to compress video files.
MP4 is a great container for exporting videos for the web, because of it exists in a single
container and has wide support across devices and operating systems.

MOV
MOV (QuickTime Movie) stores high-quality video, audio, and effects, but these files tend to be quite large. Developed for QuickTime Player by Apple, MOV files use MPEG-4 encoding to play in QuickTime for Windows. MOV is supported by Facebook and YouTube, and it works well for TV viewing.
 
WMV
WMV (Windows Media Viewer) files offer good video quality and large file size like MOV. Microsoft developed WMV for Windows Media Player. YouTube supports WMV, and Apple users can view these videos, but they must download Windows Media Player for Apple. Keep in mind you can’t select your own aspect ratio in WMV.
 
AVI
AVI (Audio Video Interleave) works with nearly every web browser on Windows, Mac, and Linux machines. Developed by Microsoft, AVI offers the highest quality but also large file sizes. It is supported by YouTube and works well for TV viewing.
 
AVCHD
Advanced Video Coding High Definition is specifically for high-definition video. Built for Panasonic and Sony digital camcorders, these files compress for easy storage without losing definition.
 
FLV, F4V, and SWF
Flash video formats FLV, F4V, and SWF (Shockwave Flash) are designed for Flash Player, but they’re commonly used to stream video on YouTube. Flash is not supported by iOS devices.
 
MKV
Developed in Russia, Matroska Multimedia Container format is free and open source. It supports nearly every codec, but it is not itself supported by many programs. MKV is a smart choice if you expect your video to be viewed on a TV or computer using an open-source media player like VLC or Miro.
 
WEBM or HTML5
These formats are best for videos embedded on your personal or business website. They are small files, so they load quickly and stream easily.
 
MPEG-2
If you want to burn your video to a DVD, MPEG-2 with an H.262 codec is the way to go.


What Is a Streaming Protocol?
Each time you watch a live stream or video on demand, streaming protocols are used to deliver data over the internet. These can sit in the application, presentation, and session layers.
Online video delivery uses both streaming protocols and HTTP-based protocols. Streaming protocols like Real-Time Messaging Protocol (RTMP) enable speedy video delivery using dedicated streaming servers, whereas HTTP-based protocols rely on regular web servers to optimize the viewing experience and quickly scale. Finally, a handful of emerging HTTP-based technologies like the Common Media Application Format (CMAF) and Apple’s Low-Latency HLS seek to deliver the best of both options to support low-latency streaming at scale.
 
UDP vs. TCP: A Quick Background
User Datagram Protocol (UDP) and Transmission Control Protocol (TCP) are both core components of the internet protocol suite, residing in the transport layer. The protocols used for streaming sit on top of these. UDP and TCP differ in terms of quality and speed, so it’s worth taking a closer look.
The primary difference between UDP and TCP hinges on the fact that TCP requires a three-way handshake when transporting data. The initiator (client) asks the accepter (server) to start a connection, the accepter responds, and the initiator acknowledges the response and maintains a session between either end. For this reason, TCP is quite reliable and can solve for packet loss and ordering. UDP, on the other hand, starts without requiring any handshake. It transports data regardless of any bandwidth constrains, making it speedier and riskier. Because UDP doesn’t support retransmissions, packet ordering, or error-checking, there’s potential for a network glitch to corrupt the data en route.
Protocols like Secure Reliable Transport (SRT) often use UDP, whereas HTTP-based protocols use TCP.
 
Considerations When Choosing a Streaming Protocol
Selecting the right protocol starts with defining what you’re trying to achieve. Latency, playback compatibility, and viewing experience can all be impacted. What’s more, content distributors don’t always stick with the same protocol from capture to playback. Many broadcasters use RTMP to get from the encoder to server and then transcode the stream into an adaptive HTTP-based format.
Traditional Streaming Protocols
Traditional streaming protocols, such as RTSP and RTMP, support low-latency streaming. But they aren’t supported on all endpoints (e.g., iOS devices). These work best for streaming to a small audience from a dedicated media server.
 
 
 
As shown above, RTMP delivers video at roughly the same pace as a cable broadcast — in just over five seconds. RTSP/RTP is even quicker at around two seconds. These protocols achieve this by transmitting the data using a firehose approach rather than requiring local download or caching. But because very few players support these protocols, they aren’t optimized for great viewing experiences at scale. Many broadcasters choose to transport live streams to the media server using a stateful protocol like RTMP and then transcode it into an HTTP-based technology for multi-device delivery.
 
Adobe RTMP
Adobe designed the RTMP specification for the transmission of audio and video data between technologies like a dedicated streaming server and the Adobe Flash Player. Reliable and low-latency, this worked great for live streaming. But open standards and adaptive bitrate streaming eventually edged RTMP out. The writing on the wall came when Adobe announced the death of Flash — slated for 2020.
While Flash’s end-of-life date is overdue, the same cannot be said for using RTMP for video contribution. RTMP encoders are still a go-to for many content producers even though the proprietary protocol has fallen out of favor for last-mile delivery.
•	Audio Codecs: AAC, AAC-LC, HE-AAC+ v1 & v2, MP3, Speex, Opus, Vorbis
•	Video Codecs: H.264, VP8, VP6, Sorenson Spark®, Screen Video v1 & v2
•	Playback Compatibility: Not widely supported (Flash Player, Adobe AIR, RTMP-compatible players)
•	Benefits: Low-latency and requires no buffering
•	Drawbacks: Not optimized for quality of experience or scalability
•	Latency: 5 seconds
•	Variant Formats: RTMPT (tunneled through HTTP), RTMPE (encrypted), RTMPTE (tunneled and encrypted), RTMPS (encrypted over SSL), RTMFP (travels over UDP instead of TCP)
 
RTSP/RTP
Like RTMP, RTSP/RTP describes a stateful protocol used for video contribution as opposed to multi-device delivery. While RTSP is a presentation-layer protocol that lets end users command media servers via pause and play capabilities, RTP is a transport protocol used to move said data.
Android and iOS devices don’t have RTSP compatible players out of the box, making this another protocol that’s rarely used for playback. That said, RTSP remains standard in many surveillance and closed-circuit television (CCTV) architectures. Why? The reason is simple. RTSP support is still ubiquitous in IP cameras.
•	Audio Codecs: AAC, AAC-LC, HE-AAC+ v1 & v2, MP3, Speex, Opus, Vorbis
•	Video Codecs: H.265 (preview), H.264, VP9, VP8
•	Playback Compatibility: Not widely supported (Quicktime Player and other RTSP/RTP-compliant players, VideoLAN VLC media player, 3Gpp-compatible mobile devices)
•	Benefits: Low-latency and supported by most IP cameras
•	Drawbacks: No longer used for video delivery to end users
•	Latency: 2 seconds
•	Variant Formats: The entire stack of RTP, RTCP (Real-Time Control Protocol), and RTSP is often referred to as RTSP
 
Adaptive HTTP-Based Streaming Protocols
Streams deployed over HTTP are not technically “streams.” Rather, they’re progressive downloads sent via regular web servers. Using adaptive bitrate streaming, HTTP-based protocols deliver the best video quality and viewer experience possible — no matter the connection, software, or device. Some of the most common HTTP-based protocols include MPEG-DASH and Apple’s HLS.
Let’s talk a bit about adaptive bitrate streaming before diving into the HTTP-Based Protocols. Adaptive Bitrate Streaming(ABR) provides the best video quality and viewer experience possible regardless of connection, device or software. It is a technique for dynamically adjusting the compression level and video quality of a stream to match bandwidth availability.  Usually, these streams are delivered via HTTP-based technologies such as MPEG DASH, HLS, CMAF and WebRTC.
 
Traditional video streaming technologies relied on distributing a fixed bitrate video stream. If your network connection could not support that bitrate, you could not watch the video without dramatic buffering. With Adaptive Bitrate Streaming, you can now stream video across the Internet, with both point to point streaming and OTT services to multiple devices.
Adaptive streaming allows the video provider to create a different video for each of the screen sizes, devices or connection speed that he or she wishes to target. 
When there are multi-bitrates on the server-side, Ant Media Server measures the viewers' internet speed and sends the best quality according to the internet speed of the viewer.  For instance,
Assume that there are two bitrates on the server
-The first one is 360p and 800kbps
-The second one is 480p and 1500kbps.
if Viewer internet speed
-is above 1500kbps, then the resolution with 480p is sent.
-is between 800kbps and 1500kbps or less than 800kbps, then the resolution with 360p is sent.

![IMAGE_DESCRIPTION](https://www.wowza.com/wp-content/uploads/Aadaptive-Bitrate-Streaming-Graphic-1.png)
 
This is done automatically on the server-side. That way, you can deliver high-quality streams to users with outstanding bandwidth and processing power, while also accommodating those lacking in the speed and power department. Rather than creating one live stream at one bitrate, a transcoder is used to create multiple streams at different bitrates and resolutions. Let’s turn back where we left.

Apple HLS
Since Apple’s a major player in the world of internet-connected devices, it follows that Apple’s HLS protocol rules the digital video landscape. For one, the protocol supports adaptive bitrate streaming, which is key to viewer experience. More importantly, a stream delivered via HLS will play back on the majority of devices — thereby expanding your audience.
While HLS support was initially limited to iOS devices such as iPhones and iPads, native support has since been added to a wide range of platforms. All Google Chrome browsers, as well as Android, Linux, Microsoft, and MacOS devices can play streams delivered using HLS.
•	Audio Codecs: AAC-LC, HE-AAC+ v1 & v2, xHE-AAC, Apple Lossless, FLAC
•	Video Codecs: H.265, H.264
•	Playback Compatibility: Great (All Google Chrome browsers; Android, Linux, Microsoft, and MacOS devices; several set-top boxes, smart TVs, and other players)
•	Benefits: Adaptive bitrate and widely supported
•	Drawbacks: Quality of experience is prioritized over low latency
•	Latency: 6-30 seconds (lower latency only possible when tuned)
•	Variant Formats: Low-Latency HLS (see below), PHLS (Protected HTTP Live Streaming)
 
Low-Latency HLS
Mid 2019, Apple announced an extension to their HLS protocol designed to drive latency down at scale. The protocol achieves this using HTTP/2 PUSH delivery combined with shorter media chunks. Unlike standard HLS, Apple Low-Latency HLS doesn’t yet support adaptive bitrate streaming — but it is on the roadmap.
•	Playback Compatibility: Any players that aren’t optimized for Low-Latency HLS can fall back to standard (higher-latency) HLS behavior
•	Benefits: Low latency meets HTTP-based streaming
•	Drawbacks: As an emerging spec, vendors are still implementing support
•	Latency: 3 seconds or less
MPEG-DASH
When it comes to MPEG-DASH, the acronym spells out the story. The Moving Pictures Expert Group (MPEG), an international authority on digital audio and video standards, developed Dynamic Adaptive Streaming over HTTP (DASH) as an industry-standard alternative to HLS. Basically, with DASH you get an open-source option. But because Apple tends to prioritize its proprietary software, support for DASH plays second fiddle.
•	Audio Codecs: Codec-agnostic
•	Video Codecs: Codec-agnostic
•	Playback Compatibility: Good (All Android devices; most post-2012 Samsung, Philips, Panasonic, and Sony TVs; Chrome, Safari, and Firefox browsers)
•	Benefits: Vendor independent, international standard for adaptive bitrate
•	Drawbacks: Not supported by iOS or Apple TV
•	Latency: 6-30 seconds (lower latency only possible when tuned)
•	Variant Formats: MPEG-DASH CENC (Common Encryption)
 
Low-Latency CMAF for DASH
The Common Media Application Format, or CMAF, is in itself is a media format. But when paired with chunked encoding and chunked transfer encoding for delivery over DASH, it should support sub-three-second delivery. While its transfer setup differs from that of Low-Latency HLS, the use of shorter data segments is quite similar.
•	Playback Compatibility: Any players that aren’t optimized for low-latency CMAF for DASH can fall back to standard (higher-latency) DASH behavior
•	Benefits: Low latency meets HTTP-based streaming
•	Drawbacks: As an emerging spec, vendors are still implementing support
•	Latency: 3 seconds or less
 
Microsoft Smooth Streaming
Microsoft developed Microsoft Smooth Streaming for use with Silverlight player applications. It enables adaptive delivery to all Microsoft devices.
•	Audio Codecs: AAC, MP3, WMA
•	Video Codecs: H.264, VC-1
•	Playback Compatibility: Good (Microsoft and iOS devices, Xbox, many smart TVs)
•	Benefits: Adaptive bitrate and supported by iOS
•	Drawbacks: Proprietary technology
•	Latency: 6-30 seconds (lower latency only possible when tuned)
 
Adobe HDS
HDS was developed for use with Flash Player applications as the first adaptive bitrate protocol. Because the end-of-life date for Flash is looming, it’s fallen out of favor.
•	Audio Codecs: AAC, MP3
•	Video Codecs: H.264, VP6
•	Playback Compatibility: Not widely supported (Flash Player, Adobe AIR)
•	Benefits: Adaptive bitrate technology for Flash
•	Drawbacks: Proprietary technology with lacking support
•	Latency: 6-30 seconds (lower latency only possible when tuned)
 
Emerging Technologies
Last but not least, new technologies like WOWZ, WebRTC, and SRT were designed with latency in mind. Similar to low-latency CMAF for DASH and Apple Low-Latency HLS, these protocols continue to evolve.
 
SRT
This open-source protocol is recognized as a proven alternative to proprietary transport technologies — helping to deliver reliable streams, regardless of network quality. From recovering lost packets to preserving timing behavior, SRT was designed to solve the challenges of video contribution and distribution across the public internet. Although it’s quickly taking the industry by storm, SRT is most often used for first-mile contribution rather than last-mile delivery.
•	Audio Codecs: Codec-agnostic
•	Video Codecs: Codec-agnostic
•	Playback Compatibility: Limited (currently used for contribution)
•	Benefits: High-quality, low-latency video over suboptimal networks
•	Drawbacks: Playback support is still in the works
•	Latency: 3 seconds or less
 
WebRTC
WebRTC is a combination of standards, protocols, and JavaScript APIs that enables real-time communications (RTC, hence its name). Users connecting via Chrome, Firefox, or Safari can communicate directly through their browsers — enabling sub-500 millisecond latency. According to Google, “with Chrome, Edge, Firefox, and Safari supporting WebRTC, more than 85% of all installed browsers globally have become a client for real-time communications on the internet.” WebRTC is actually a technology that enables live video streaming via web browser without the need for streaming video server.
Therefore, if you use WebRTC technology, in a way, you have the opportunity to stream live in a "serverless" architecture. Since there is such a technology, why do we need costly servers for live streaming. The answer is actually simple: WebRTC provides data exchange in the form of browser to browser, so if you try to streaming over WebRTC with 10 people at the same time, it is likely that the internet bandwidth in your home will not be sufficient and therefore you will not be able to stream this video at the same time. Broadcaster cannot provide this over its own internet connection, streaming can be provided first to the server with WebRTC, then to other viewers via the server with a broad bandwidth of the server.

 
•	Audio Codecs: Opus, iSAC, iLBC
•	Video Codecs: H.264, VP8, VP9
•	Playback Compatibility: Chrome, Firefox, and Safari support WebRTC without any plugin
•	Benefits: Super fast and browser-based
•	Drawbacks: Designed for video conferencing and not scale
•	Latency: Sub-500-millisecond delivery





References

Adaptive Bitrate Streaming. (n.d.). Antmedia. Retrieved February 10, 2021, from https://antmedia.io/adaptive-bitrate-streaming/
Best Video Format. (n.d.). Adobe.Com. Retrieved February 10, 2021, from https://www.adobe.com/creativecloud/video/discover/best-video-format.html
FFmpeg. (n.d.). Wikipedia. Retrieved February 10, 2021, from https://en.wikipedia.org/wiki/FFmpeg
How Streaming Video and Audio Work. (n.d.). Howstuffworks. Retrieved February 10, 2021, from https://computer.howstuffworks.com/internet/basics/streaming-video-and-audio.htm#pt1
Ölçeklemek önemlidir. WebRTC yayınları v1.4 ile ölçeklenebilir. (n.d.). Antmedia. Retrieved February 10, 2021, from https://antmedia.io/olceklemek-onemlidir-webrtc-yayin-ant-media-server-ile-olceklenebilir/
Streaming Protocols. (n.d.). Wowza. Retrieved February 10, 2021, from https://www.wowza.com/blog/streaming-protocols#rtmp
Video Formats, Codecs and Containers. (n.d.). Youtube. Retrieved February 10, 2021, from https://www.youtube.com/watch?v=XvoW-bwIeyY
What is Video Bitrate. (n.d.). Restream. Retrieved February 10, 2021, from https://restream.io/blog/what-is-video-bitrate/

