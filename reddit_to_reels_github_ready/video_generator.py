from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip

def create_video_with_audio_and_subtitle(audio_file, subtitle_text, output_file='output.mp4'):
    gameplay_video = VideoFileClip('assets/gameplay_loop.mp4').subclip(0, 60)
    audio = AudioFileClip(audio_file)

    subtitle = TextClip(subtitle_text, fontsize=24, color='white', bg_color='black', size=gameplay_video.size, method='caption')
    subtitle = subtitle.set_position(('center', 'bottom')).set_duration(audio.duration)

    final_video = CompositeVideoClip([gameplay_video, subtitle])
    final_video = final_video.set_audio(audio)
    final_video.write_videofile(output_file, codec='libx264')