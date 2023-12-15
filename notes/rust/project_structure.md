In rust all files and folders are **modules**.  
All Rust projects are **crates**.  
The `crate::` prefix indicates the root of the project.  

Everything inside a module can access anything else in that same module.  
Everything outside that module can only access public members of that module.  


# mod.rs

in each folder you create, you include a `mod.rs` file that has lines like:

```rust
mod submodule1;
mod submodule2;
```

for each submodule.

### Sources

(1)[https://medium.com/codex/rust-modules-and-project-structure-832404a33e2e]
