import * as anchor from "@project-serum/anchor";
import { Program } from "@project-serum/anchor";
import { PrestigeProgram } from "../target/types/prestige_program";

describe("prestige_program", () => {
  // Configure the client to use the local cluster.
  anchor.setProvider(anchor.AnchorProvider.env());

  const program = anchor.workspace.PrestigeProgram as Program<PrestigeProgram>;

  it("Is initialized!", async () => {
    // Add your test here.
    const tx = await program.methods.initialize().rpc();
    console.log("Your transaction signature", tx);
  });
});
