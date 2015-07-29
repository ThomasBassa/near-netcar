import trollius as asyncio

@asyncio.coroutine
def do(thing):
	while True:
		print thing
		yield asyncio.sleep(.5)

loop = asyncio.get_event_loop()
swag = asyncio.new_event_loop()
asyncio.set_event_loop(swag)
tasks = [
	asyncio.async(do("This is task 1")),
	asyncio.async(do("This is task 2"))]
swag.run_until_complete(asyncio.wait(tasks))
