Generate 10 new SMILES strings for extractants which separate Eu from Am. Generated molecules will be evaluated by the following criteria:

1. Distribution coefficient for the target metal Am(III) should be high, corresponding to Target_metal = ORGANIC.
2. Distribution coefficient for the other metal Eu(III) should be low, corresponding to Other_metal = AQUEOUS.
3. Similarity to SMILES where Source = Experimental, as evaluated by Tanimoto similarity of ECFP fingerprint, should favor novel molecules with medium similarity in the range between 0.25 and 0.85.
4. Similarity to SMILES where Source = LLM generated, as evaluated by Tanimoto similarity of ECFP fingerprint, should favor novel molecules with low or medium similarity smaller than 0.85.
5. Organic/Water Partitioning (LogP), should favor LogP = ORGANIC phase with LogP value larger than 3.

## Goal

1. Create novel extractant structures where Target_metal = ORGANIC and Other_metal = AQUEOUS and LogP = ORGANIC by learning from the examples where Source = Experimental in the SMILES Evaluation Status Table.
2. Consider the following design focus: {design-focus}.
3. Apply modifications such as replacing, mixing, or changing side chains, functional groups, and/or backbone structures to ensure diversity.
4. Propose structurally diverse extractants that vary from those in the table and meet all criteria and constraints above.
5. Propose easy to synthesize and chemically accessible molecules.
6. Propose stable molecules which are resistant to strong acids and radiolysis.

## Current SMILES Evaluation Status Table (JSON Format)

See `../../eval/data_list.txt` for the reference table (Source = Experimental entries) sent alongside this prompt.
