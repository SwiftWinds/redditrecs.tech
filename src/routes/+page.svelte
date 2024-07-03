<script lang="ts">
	import { goto } from '$app/navigation';

	let query = '';
	let suggestions: string[] = [];

	async function getSuggestions() {
		const res = await fetch(
			`http://localhost:5001/redditrecs-tech/us-central1/get_suggestions?q=${query}`
		);
		suggestions = await res.json();
	}
</script>

<form autocomplete="off" on:submit|preventDefault={() => goto(`/search?q=${query}`)}>
	<input type="text" name="q" id="q" bind:value={query} on:keyup={getSuggestions} />
	<div id="result">
		<ul>
			{#each suggestions as suggestion}
				<li>{@html suggestion}</li>
			{/each}
		</ul>
	</div>
	<button type="submit">Go</button>
</form>

<style>
	#result {
		border: 1px dotted #ccc;
		padding: 3px;
	}
	#result ul {
		list-style-type: none;
		padding: 0;
		margin: 0;
	}
	#result ul li {
		padding: 5px 0;
	}
	#result ul li:hover {
		background: #eee;
	}
</style>
