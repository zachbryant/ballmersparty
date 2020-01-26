export default function ({
  store,
  redirect
}) {
  if (!store.state.party.global.join_code) {
    redirect("/")
  }
}
