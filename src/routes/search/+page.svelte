<script lang="ts">
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import { db } from '$lib/firebase';
	import { onSnapshot, doc, getDoc, setDoc } from 'firebase/firestore';
	import type { Unsubscribe } from 'firebase/firestore';

	let query = '';

	interface Recommendation {
		name: string;
	}

	interface QueryData {
		status: 'loading' | 'success' | 'error';
		results: Recommendation[];
	}

	let data: QueryData = {
		status: 'loading',
		results: []
	};

	const MONTH_IN_MS = 30 * 24 * 60 * 60 * 1000;

	onMount(() => {
		let unsub: undefined | Unsubscribe;

		async function submitQuery() {
			const queryRef = doc(db, `queries/${query}`);
			const queryDoc = await getDoc(queryRef);
			if (!queryDoc.exists || queryDoc.get('lastUpdated').toMillis() < Date.now() - MONTH_IN_MS) {
				await setDoc(queryRef, { status: 'loading', lastUpdated: new Date() });
			}
			unsub = onSnapshot(queryRef, (doc) => {
				data = { ...data, ...doc.data() };
			});
		}

		query = $page.url.searchParams.get('q') ?? '';
		submitQuery();
		return () => unsub?.();
	});
</script>

{#if data.status === 'loading'}
	<p>Loading...</p>
{:else if data.status === 'error'}
	<p>Error</p>
{:else}
	<ul>
		{#each data.results as result}
			<li>{result.name}</li>
		{/each}
	</ul>
{/if}
