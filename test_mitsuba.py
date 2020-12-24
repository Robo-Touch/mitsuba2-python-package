try:
	import mitsuba
	mitsuba.set_variant("packet_rgb")
	from mitsuba.core import *
	from mitsuba.render import *
except ImportError:
	print("Unable to load mitsuba")