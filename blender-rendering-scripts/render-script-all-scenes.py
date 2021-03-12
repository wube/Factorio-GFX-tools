import bpy
import time
import datetime

### timestamp creation ----------------------------------------------

print('-'*36)
print('Starting...')

time_started = time.time()
time_started_formatted = datetime.datetime.fromtimestamp(time_started).strftime('%H:%M:%S')







###
### RENDERING ----------------------------------------------
###

for scene in bpy.data.scenes:
  bpy.context.window.scene = scene
  
  print(scene.name)
  #bpy.ops.vtools.render_multicomputer()
  #bpy.ops.vtools.generate_render_nodes()
  bpy.ops.render.render(animation=True)
 









### timestamp creation -----------------------------------------------
  
time_finished = time.time()
time_finished_formatted = datetime.datetime.fromtimestamp(time_finished).strftime('%H:%M:%S')

time_elapsed = time_finished - time_started
time_elapsed_formatted = str(datetime.timedelta(seconds=int(time_elapsed)))

print('Finished!')
print('Time started:  ' + time_started_formatted)
print('Time finished: ' + time_finished_formatted)
print('Time elapsed:  ' + time_elapsed_formatted)

