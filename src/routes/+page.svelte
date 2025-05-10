<script lang="ts">
	let chatbot: HTMLIFrameElement;
	const iframeSource = 'http://127.0.0.1:8000/';

	// eslint-disable-next-line @typescript-eslint/no-explicit-any
	function handleMessage(event: MessageEvent<any>) {
		if (event.data.startsWith('Server: ')) {
			console.log('Parent window received:', event.data);
			postMessageToIframe(event.data);
		}
	}

	function postMessageToIframe(message: string) {
		chatbot.contentWindow?.postMessage(`Client: ${message}`, iframeSource);
	}
</script>

<svelte:window onmessage={handleMessage} />

<iframe
	bind:this={chatbot}
	title="chatbot"
	src={iframeSource}
	data-cy="the-frame"
	width="100%"
	height="500px"
></iframe>
